def _run_child(self, cmd):
    if type(cmd) == type(''):
        cmd = ['/bin/sh', '-c', cmd]