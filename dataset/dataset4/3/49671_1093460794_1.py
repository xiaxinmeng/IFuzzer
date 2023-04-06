# these will fail with above error message
my_socket.sendto("No Umlaut", ("localhost", 514))
my_socket.sendto(1, ("localhost", 514))