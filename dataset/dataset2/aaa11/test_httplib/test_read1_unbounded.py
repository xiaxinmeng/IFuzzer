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

def test_read1_unbounded():
    resp = ExtendedReadTest.resp
    all = []
    while True:
        data = resp.read1()
        if not data:
            break
        all.append(data)
    ExtendedReadTest.assertEqual(b''.join(all), ExtendedReadTest.lines_expected)

ExtendedReadTest = test_httplib.ExtendedReadTest()
ExtendedReadTest.setUp()
test_read1_unbounded()
