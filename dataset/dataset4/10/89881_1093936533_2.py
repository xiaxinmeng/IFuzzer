class PatchedMultiLoopChildWatcher(asyncio.MultiLoopChildWatcher):
    "Test race condition fixes in MultiLoopChildWatcher."

    def add_child_handler(self, pid, callback, *args):
        loop = asyncio.get_running_loop()
        self._callbacks[pid] = (loop, callback, args)

        # Prevent a race condition in case signal was delivered before
        # callback added.
        signal.raise_signal(signal.SIGCHLD)

    @_serialize
    def _sig_chld(self, signum, frame):
        super()._sig_chld(signum, frame)