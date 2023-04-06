class catch_unraisable_exception:
    def __init__(self):
        self.unraisable = None
        self._old_hook = None

    def _hook(self, unraisable):
        self.unraisable = unraisable

    def __enter__(self):
        self._old_hook = sys.unraisablehook
        sys.unraisablehook = self._hook
        return self

    def __exit__(self, *exc_info):
        # Clear the unraisable exception to explicitly break a reference cycle
        del self.unraisable
        sys.unraisablehook = self._old_hook