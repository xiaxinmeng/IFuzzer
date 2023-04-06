if hasattr(errno, 'EADDRNOTAVAIL'):
    # socket.create_connection() fails randomly with
    # EADDRNOTAVAIL on Travis CI.
    expected_errnos.append(errno.EADDRNOTAVAIL)