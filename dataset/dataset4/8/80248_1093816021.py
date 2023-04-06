def terminate(self):
    """Terminates the process."""
    # Don't terminate a process that we know has already died.
    if self.returncode is not None:
        return
    try:
        _winapi.TerminateProcess(self._handle, 1)
    except WindowsError as err:
        if err.errno in (ERROR_ACCESS_DENIED, ERROR_INVALID_HANDLE):
            rc = _winapi.GetExitCodeProcess(self._handle)
            if rc == _winapi.STILL_ACTIVE:
                raise
            self.returncode = rc
        else:
            raise