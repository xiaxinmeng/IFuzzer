def my_trivial_socket_function(address_tuple, a=None):
    host, port = address_tuple
    for result in getaddrinfo(host, port, 0, 0, 0):
        whatever(*result)