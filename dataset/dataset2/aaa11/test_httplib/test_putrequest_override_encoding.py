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

def test_putrequest_override_encoding():
    """
        It should be possible to override the default encoding
        to transmit bytes in another encoding even if invalid
        (bpo-36274).
        """

    class UnsafeHTTPConnection(client.HTTPConnection):

        def _encode_request(BasicTest, str_url):
            return str_url.encode('utf-8')
    conn = UnsafeHTTPConnection('example.com')
    conn.sock = test_httplib.FakeSocket('')
    conn.putrequest('GET', '/☃')

BasicTest = test_httplib.BasicTest()
test_putrequest_override_encoding()
