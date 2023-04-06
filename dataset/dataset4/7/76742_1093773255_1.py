async def op(self, *args):
    while True:
        try:
            # First try fulfilling the operation from cache
            MAGIC_THREAD_LOCAL.io_is_forbidden = True
            return self._io_obj.op(*args)
        except IOForbiddenError as exc:
            # We have to actually hit the disk
            # Run the real IO operation in a thread, then try again
            await in_thread(cache_filler)
        finally:
            del MAGIC_THREAD_LOCAL.io_is_forbidden