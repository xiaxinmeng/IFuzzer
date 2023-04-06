def connect():
    try:
        s.connect(('people.csail.mit.edu', 443))
    except socket.error as e:
        if e.errno != errno.EINPROGRESS:
            raise
        return False
    else:
        return True

while not connect():
    select.select([s], [s], [])

while True:
    try:
        select.select([s], [s], [])
        s.do_handshake()
        break
    except ssl.SSLError as err:
        if err.args[0] == ssl.SSL_ERROR_WANT_READ:
            select.select([s], [], [])
        elif err.args[0] == ssl.SSL_ERROR_WANT_WRITE:
            select.select([], [s], [])
        else:
            raise