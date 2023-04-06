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

def test_getting_nonexistent_header_with_iterable_default():
    header = HTTPResponseTest.resp.getheader('No-Such-Header', ['default', 'values'])
    HTTPResponseTest.assertEqual(header, 'default, values')
    header = HTTPResponseTest.resp.getheader('No-Such-Header', ('default', 'values'))
    HTTPResponseTest.assertEqual(header, 'default, values')

HTTPResponseTest = test_httplib.HTTPResponseTest()
HTTPResponseTest.setUp()
test_getting_nonexistent_header_with_iterable_default()
