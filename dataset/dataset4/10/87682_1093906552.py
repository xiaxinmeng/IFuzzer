import socket

HOST = "192.168.2.114"
PORT = 8000 #initiate port no above 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#try:
s.bind((HOST, PORT))  #bind host address and port together#
#except socket.error as e:
    #print('Bind failed.')
    
s.listen(10)  #configure how many clients the server can listen to simultaneously

print("Socket is Listening")
 
#conn, addr = s.accept()    #accept new connection
#print("connection from:" + str(addr))
    