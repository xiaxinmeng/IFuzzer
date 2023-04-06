# Bug demo
TEXT_LINES = [
    b'cutecat\n',
    b'promiscuousbonobo\n',
]
TEXT = b''.join(TEXT_LINES)
import bz2
filename = '/tmp/demo.bz2'
with open(filename, 'wb') as f:
    f.write(bz2.compress(TEXT))

with bz2.BZ2File(filename) as bz2f:
    pdata = bz2f.peek(n=7)
    print(pdata)