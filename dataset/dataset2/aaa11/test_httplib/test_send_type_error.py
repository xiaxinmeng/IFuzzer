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

def test_send_type_error():
    conn = client.HTTPConnection('example.com')
    conn.sock = test_httplib.FakeSocket('')
    with BasicTest.assertRaises(TypeError):
        conn.request('POST', 'test', conn)

BasicTest = test_httplib.BasicTest()
test_send_type_error()
