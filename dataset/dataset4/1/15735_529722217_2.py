def close(self):
    ...
    self._closed = True
    self._ready.clear()
    self._scheduled.clear()
#    executor = self._default_executor
#    if executor is not None:
#        self._default_executor = None
#        executor.shutdown(wait=self._wait_executor_on_close)
    self.shutdown_default_executor() # default is True