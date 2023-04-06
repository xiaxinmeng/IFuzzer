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

def test_putrequest_override_host_validation():

    class UnsafeHTTPConnection(client.HTTPConnection):

        def _validate_host(BasicTest, url):
            pass
    conn = UnsafeHTTPConnection('example.com\r\n')
    conn.sock = test_httplib.FakeSocket('')
    conn.putrequest('GET', '/', skip_host=1)

BasicTest = test_httplib.BasicTest()
test_putrequest_override_host_validation()
