import errno
from http import client, HTTPStatus
import io
import itertools
import os
import array
import re
import socket
import threading
import warnings
import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import warnings_helper
from test.ssl_servers import make_https_server
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import test_httplib

def test_putheader():
    conn = client.HTTPConnection('example.com')
    conn.sock = test_httplib.FakeSocket(None)
    conn.putrequest('GET', '/')
    conn.putheader('Content-length', 42)
    HeaderTests.assertIn(b'Content-length: 42', conn._buffer)
    conn.putheader('Foo', ' bar ')
    HeaderTests.assertIn(b'Foo:  bar ', conn._buffer)
    conn.putheader('Bar', '\tbaz\t')
    HeaderTests.assertIn(b'Bar: \tbaz\t', conn._buffer)
    conn.putheader('Authorization', 'Bearer mytoken')
    HeaderTests.assertIn(b'Authorization: Bearer mytoken', conn._buffer)
    conn.putheader('IterHeader', 'IterA', 'IterB')
    HeaderTests.assertIn(b'IterHeader: IterA\r\n\tIterB', conn._buffer)
    conn.putheader('LatinHeader', b'\xff')
    HeaderTests.assertIn(b'LatinHeader: \xff', conn._buffer)
    conn.putheader('Utf8Header', b'\xc3\x80')
    HeaderTests.assertIn(b'Utf8Header: \xc3\x80', conn._buffer)
    conn.putheader('C1-Control', b'next\x85line')
    HeaderTests.assertIn(b'C1-Control: next\x85line', conn._buffer)
    conn.putheader('Embedded-Fold-Space', 'is\r\n allowed')
    HeaderTests.assertIn(b'Embedded-Fold-Space: is\r\n allowed', conn._buffer)
    conn.putheader('Embedded-Fold-Tab', 'is\r\n\tallowed')
    HeaderTests.assertIn(b'Embedded-Fold-Tab: is\r\n\tallowed', conn._buffer)
    conn.putheader('Key Space', 'value')
    HeaderTests.assertIn(b'Key Space: value', conn._buffer)
    conn.putheader('KeySpace ', 'value')
    HeaderTests.assertIn(b'KeySpace : value', conn._buffer)
    conn.putheader(b'Nonbreak\xa0Space', 'value')
    HeaderTests.assertIn(b'Nonbreak\xa0Space: value', conn._buffer)
    conn.putheader(b'\xa0NonbreakSpace', 'value')
    HeaderTests.assertIn(b'\xa0NonbreakSpace: value', conn._buffer)

HeaderTests = test_httplib.HeaderTests()
test_putheader()
