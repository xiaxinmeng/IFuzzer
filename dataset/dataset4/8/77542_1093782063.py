
from __future__ import print_function

import codecs
import io


def run(stream):
    offset = stream.tell()
    try:
        stream.seek(0)
        header_row = stream.readline()
    finally:
        stream.seek(offset)
    print(offset)
    print(stream.tell())
    print('Got header: %r' % header_row)

    if stream.tell() == 0:
        print(stream.tell())
        print(stream.readline())
        print('Skipping the header: %r' % stream.readline())

    for index, line in enumerate(stream, start=2):
        print('Line %d: %r' % (index, line))


b = io.BytesIO(u'ab\r\ncd\ndef\n'.encode('utf-16-le'))
s = codecs.EncodedFile(b, 'utf-8', 'utf-16-le')
run(s)

