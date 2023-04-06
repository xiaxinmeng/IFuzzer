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

def test_100_close():
    conn = test_httplib.FakeSocketHTTPConnection(b'HTTP/1.1 100 Continue\r\n\r\n')
    conn.request('GET', '/', headers={'Expect': '100-continue'})
    PersistenceTest.assertRaises(client.RemoteDisconnected, conn.getresponse)
    PersistenceTest.assertIsNone(conn.sock)
    conn.request('GET', '/reconnect')
    PersistenceTest.assertEqual(conn.connections, 2)

PersistenceTest = test_httplib.PersistenceTest()
test_100_close()
