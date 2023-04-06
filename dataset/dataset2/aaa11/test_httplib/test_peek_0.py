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

def test_peek_0():
    p = ExtendedReadTest.resp.peek(0)
    ExtendedReadTest.assertLessEqual(0, len(p))

ExtendedReadTest = test_httplib.ExtendedReadTest()
ExtendedReadTest.setUp()
test_peek_0()
