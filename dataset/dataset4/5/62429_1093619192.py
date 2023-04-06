#minimal server:
#!/c/Python33/python.exe
from http.server import HTTPServer as S, BaseHTTPRequestHandler as H
class HNDL(H):
	def log_request(req,code):
		print('header is',req.headers.get('X-Forwarder-For'),', code',code)
		H.log_request(req)
s=S(('',54321),HNDL)
s.serve_forever()


#non-http client:
#!/c/Python33/python.exe
import socket,os
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 54321))
s.sendall(os.urandom(1024))
buf=s.recv(2048)
s.close()
print(buf)