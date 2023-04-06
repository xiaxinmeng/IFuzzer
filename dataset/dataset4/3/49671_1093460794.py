# this will succeed
my_socket.sendto("Foobar", ("localhost", 514))

# these will fail with above error message
my_socket.sendto(u"Umlaut ä", ("localhost", 514))
my_socket.sendto(1, ("localhost", 514))