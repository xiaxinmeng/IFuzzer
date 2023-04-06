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

def test_networked():
    import ssl
    support.requires('network')
    with socket_helper.transient_internet('HTTPSTest-signed.pythontest.net'):
        h = client.HTTPSConnection('HTTPSTest-signed.pythontest.net', 443)
        with HTTPSTest.assertRaises(ssl.SSLError) as exc_info:
            h.request('GET', '/')
        HTTPSTest.assertEqual(exc_info.exception.reason, 'CERTIFICATE_VERIFY_FAILED')

HTTPSTest = test_httplib.HTTPSTest()
test_networked()
