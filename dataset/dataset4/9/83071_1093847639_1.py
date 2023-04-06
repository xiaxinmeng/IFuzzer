popen = subprocess.Popen(args, creationflags=DETACHED_PROCESS)
print('Running daemon process: ', popen.pid)
# Set the returncode to avoid erroneous warning:
# "ResourceWarning: subprocess XXX is still running".
popen.returncode = 0
del popen