pytb
"""
Traceback (most recent call last):
  File "z.py", line 8, in <module>
    s = ssl.wrap_socket(s)
  File "/usr/local/lib/python2.7/ssl.py", line 372, in wrap_socket
    ciphers=ciphers)
  File "/usr/local/lib/python2.7/ssl.py", line 134, in __init__
    self.do_handshake()
  File "/usr/local/lib/python2.7/ssl.py", line 296, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [Errno 2] _ssl.c:503: The operation did not complete (read)
"""
