
def _set_socket_extra(transport, sock):
    transport._extra['socket'] = trsock.TransportSocket(sock)

    try:
        transport._extra['sockname'] = sock.getsockname()
    except socket.error:
        if transport._loop.get_debug():
            logger.warning(
                "getsockname() failed on %r", sock, exc_info=True)

    if 'peername' not in transport._extra:
        try:
            transport._extra['peername'] = sock.getpeername()
        except socket.error:
            # UDP sockets may not have a peer name
            transport._extra['peername'] = None
