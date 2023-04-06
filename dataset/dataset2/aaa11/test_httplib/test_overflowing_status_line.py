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

def test_overflowing_status_line():
    body = 'HTTP/1.1 200 Ok' + 'k' * 65536 + '\r\n'
    resp = client.HTTPResponse(test_httplib.FakeSocket(body))
    BasicTest.assertRaises((client.LineTooLong, client.BadStatusLine), resp.begin)

BasicTest = test_httplib.BasicTest()
test_overflowing_status_line()
