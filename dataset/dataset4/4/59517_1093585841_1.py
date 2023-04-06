HOST = '216.240.155.229'    # The remote host
PORT = 9090              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
ser = serial.Serial('USB0', timeout=3)
x = 0
#while x < 5:
while True:
    msg = ser.readline()
    s.send(msg)
    x += 1
s.close()