# test_flock.py
import fcntl

def lock(fd, flags):
    fcntl.flock(fd.fileno(), flags)

def unlock(fd):
    fcntl.flock(fd.fileno(), fcntl.LOCK_UN)

fd = open('test.txt', 'w')
lock(fd, fcntl.LOCK_SH)
fd.write('testing')
unlock(fd)
fd.close()
# end of test_flock.py