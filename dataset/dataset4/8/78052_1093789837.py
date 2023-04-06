import os
fo = open('/tmp/temp', 'wb')
fi = open('/tmp/temp', 'rb')
os.sendfile(fo.fileno(), fi.fileno(), 0, 0, headers=[b'x' * 2**16] * 2**15)