#3.5.3
import socket
s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(('vcan0',)) # requires tuple
s.getsockname() # returns tuple: ('vcan0', 29)

#3.7.3
import socket
s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
s.bind(('vcan0',)) # requires tuple
s.getsockname() # returns string: 'vcan0'