sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.connect('/dev/log')
sock.send(MSG1)
os.close(sock.fileno()) # what daemonizing does
try:
    sock.send(MSG2)
except socket.error as e:
    print(e)
    print('Trying to reconnect:')
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        sock.connect('/dev/log')
    except socket.error as e:
        print('Oh look, reconnecting failed: %s' % e)