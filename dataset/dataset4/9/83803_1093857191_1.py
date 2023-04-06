# in class BaseEventLoop
def _check_interrupted(self):
    # This will be called by BaseEventLoop._run_once() before calling select,
    # and before popping any handle from the ready queue
    if self._interrupted:
        raise KeyboardInterrupt