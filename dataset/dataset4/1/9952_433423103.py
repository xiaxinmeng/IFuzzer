
while not self.__shutdown_request:
    # XXX: Consider using another file descriptor or
    # connecting to the socket to wake this up instead of
    # polling. Polling reduces our responsiveness to a
    # shutdown request and wastes cpu at all other times.
    r, w, e = _eintr_retry(select.select, [self], [], [],
                           poll_interval)
    if self in r:
        self._handle_request_noblock()
