import http.client
import time

def test(connection_class=http.client.HTTPSConnection, timeout=10, read_size=7):
    start = time.time()
    c = connection_class('sleepy-reaches-6892.herokuapp.com')
    c.connect()
    if timeout is not None:
        c.sock.settimeout(timeout)
    c.request('GET', '/test')
    r = c.getresponse()
    while True:
        data = r.read(read_size)
        if not data:
            break
    print('Finished in {}'.format(time.time() - start))