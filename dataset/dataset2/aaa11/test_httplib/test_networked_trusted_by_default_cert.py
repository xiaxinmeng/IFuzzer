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

@support.system_must_validate_cert
def test_networked_trusted_by_default_cert():
    support.requires('network')
    with socket_helper.transient_internet('www.python.org'):
        h = client.HTTPSConnection('www.python.org', 443)
        h.request('GET', '/')
        resp = h.getresponse()
        content_type = resp.getheader('content-type')
        resp.close()
        h.close()
        HTTPSTest.assertIn('text/html', content_type)

HTTPSTest = test_httplib.HTTPSTest()
test_networked_trusted_by_default_cert()
