import fcntl, sys
fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL,
os.O_NONBLOCK)