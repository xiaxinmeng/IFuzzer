for i in range(20):
  control_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  control_socket.connect(("www.google.com", 80))
  control_socket_file = control_socket.makefile(mode = "rw", newline = "") 

  Demo(control_socket_file)