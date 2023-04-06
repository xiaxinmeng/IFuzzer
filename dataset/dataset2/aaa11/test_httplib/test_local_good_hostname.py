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

def test_local_good_hostname():
    import ssl
    server = HTTPSTest.make_server(test_httplib.CERT_localhost)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(CERT_localhost)
    h = client.HTTPSConnection('localhost', server.port, context=context)
    HTTPSTest.addCleanup(h.close)
    h.request('GET', '/nonexistent')
    resp = h.getresponse()
    HTTPSTest.addCleanup(resp.close)
    HTTPSTest.assertEqual(resp.status, 404)

HTTPSTest = test_httplib.HTTPSTest()
test_local_good_hostname()
