# No error raised.
def func():
    lockfile = open('lockfile', 'w')
    fcntl.flock(lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
    input() # no error raised, can be sleep etc..


func()

# Error raised.
lockfile = open('lockfile', 'w')
fcntl.flock(lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
input() # no error raised