def wrapped_op(self, *args):
    if self._cached_op.key == (op, args):
        return self._cached_op.result
    if MAGIC_THREAD_LOCAL.io_is_forbidden:
        def cache_filler():
            MAGIC_THREAD_LOCAL.io_is_forbidden = False
            self._cached_op = self._real_file.op(*args)
        raise IOForbiddenError(cache_filler)
    return self._real_file.op(*args)