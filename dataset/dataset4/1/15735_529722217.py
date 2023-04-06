def shutdown_default_executor(self, wait=True):
    # Used by loop.run_in_executer() to check if the the executor has been terminated
    self._executor_shutdown_called = True 
    executor = self._default_executor
    # Nothing to shut down if there is no executor
    if executor is not None: 
        self._default_executor = None
        executor.shutdown(wait) # alternatively, wait=wait, but that seems redundant