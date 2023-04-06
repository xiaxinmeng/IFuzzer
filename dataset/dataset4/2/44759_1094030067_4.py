def my_trivial_socket_function(address_tuple,a=None):
    assert type(address_tuple) is type( () )
    assert type(address_tuple[0]) is type("")
    assert type(address_tuple[1]) is type(0)
    host, port = address_tuple
    for result in getaddrinfo(host, port, 0, 0, 0):
        pass