while self._read_set or self._write_set:
    timeout = self._remaining_time(endtime)
    if timeout is not None and timeout < 0:
        raise TimeoutExpired(self.args, orig_timeout)
    try:
        (rlist, wlist, xlist) = \
            select.select(self._read_set, self._write_set, [],
                          timeout)
    except select.error as e:
        if e.args[0] == errno.EINTR:
            continue
        raise
    ...