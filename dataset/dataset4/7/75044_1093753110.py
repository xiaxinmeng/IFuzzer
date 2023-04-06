import socket
import time

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 6379))

# give enought time to get the
# data plus the RST Package
time.sleep(1)

# read the data
print(s.recv(100))