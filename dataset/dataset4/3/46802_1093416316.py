def bind_port(sock, host=''):
    """Bind the socket to a free port and return the port number.
    Relies on ephemeral ports in order to ensure we are using an
    unbound port.  This is important as many tests may be running
    simultaneously, especially in a buildbot environment."""

    # Use a temporary socket object to ensure we're not 
    # affected by any socket options that have already 
    # been set on the 'sock' object we're passed. 
    tempsock = socket.socket(sock.family, sock.type)
    tempsock.bind((host, 0))
    port = tempsock.getsockname()[1]
    tempsock.close()
    del tempsock

    sock.bind((host, port))
    return port