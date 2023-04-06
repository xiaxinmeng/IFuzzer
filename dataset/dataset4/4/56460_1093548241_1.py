# Dup fds for child
if p2cread is not None:
    os.dup2(p2cread, 0)
if c2pwrite is not None:
    os.dup2(c2pwrite, 1)
if errwrite is not None:
    os.dup2(errwrite, 2)

# Close pipe fds.  Make sure we don't close the same
# fd more than once, or standard fds.
if p2cread is not None and p2cread not in (0,):
    os.close(p2cread)
if c2pwrite is not None and c2pwrite not in (p2cread, 1):
    os.close(c2pwrite)
if errwrite is not None and errwrite not in (p2cread, c2pwrite, 2):
    os.close(errwrite)