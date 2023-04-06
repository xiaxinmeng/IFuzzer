
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

    print('Got header: %r' % header_row)

    if stream.tell() == 0:
        print('Skipping the header: %r' % stream.readline())

    for index, line in enumerate(stream, start=2):
        print('Line %d: %r' % (index, line))


b = io.BytesIO(u'a,b\r\n"asdf","jkl;"\r\n'.encode('utf-16-le'))
s = codecs.EncodedFile(b, 'utf-8', 'utf-16-le')

run(s)
