DETACHED_PROCESS = getattr(subprocess, 'DETACHED_PROCESS', 0x00000008)
popen = subprocess.Popen(args, creationflags=DETACHED_PROCESS)
print('Running daemon process: ', popen.pid)
del popen