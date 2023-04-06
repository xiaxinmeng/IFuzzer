# Close pipe fds. Make sure we don't close the
# same fd more than once, or standard fds.
closed = set()
for fd in [p2cread, c2pwrite, errwrite]:
    if fd > 2 and fd not in closed:
        os.close(fd)
        closed.add(fd)