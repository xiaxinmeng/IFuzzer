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

def test_read_head():
    sock = test_httplib.FakeSocket('HTTP/1.1 200 OK\r\nContent-Length: 14432\r\n\r\n', test_httplib.NoEOFBytesIO)
    resp = client.HTTPResponse(sock, method='HEAD')
    resp.begin()
    if resp.read():
        BasicTest.fail('Did not expect response from HEAD request')

BasicTest = test_httplib.BasicTest()
test_read_head()
