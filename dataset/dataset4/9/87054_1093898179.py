import socket
from threading import Thread
class thread(Thread):
      def run(self):
          for res in socket.getaddrinfo('www.google.com',8080):
              sock = socket.socket()
              sock.connect(res[4])

for i in range(2000):
    thread().start()