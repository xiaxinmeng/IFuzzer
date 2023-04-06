class Pid:
    def __init__(self, pid):
        self._pid = pid

    def pidno(self):
        return self._pid

    def closed(self):
        return self._pid != -1

    def reap(self):
        with self._lock:  # _pyio.FileIO is probably missing this lock
             pid = self._pid
             self._pid = -1
        os.waitpid(pid, ...)