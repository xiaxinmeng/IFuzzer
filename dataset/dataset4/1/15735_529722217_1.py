def _check_executor_shutdown(self):
    if self._executor_shutdown_called:
        raise RuntimeError("Executor has been shut down")