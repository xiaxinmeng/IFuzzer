if flags:
    # Only check for exceptions if object was either readable
    # or writable.
    flags |= select.POLLERR | select.POLLHUP | select.POLLNVAL
    pollster.register(fd, flags)