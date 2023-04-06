import socket
import warnings

def show(msg):
    s = msg.source
    #s.close()
    if s.fileno() >= 0:
        print("socket open")
    else:
        print("socket closed")
    try:
        name = s.getsockname()
    except Exception as exc:
        name = str(exc)
    print("getsockname(): %r" % (name,))

warnings._showwarnmsg = show
s = socket.socket()
s = None