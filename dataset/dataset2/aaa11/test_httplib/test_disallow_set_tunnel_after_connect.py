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

def test_disallow_set_tunnel_after_connect():
    TunnelTests.conn.connect()
    TunnelTests.assertRaises(RuntimeError, TunnelTests.conn.set_tunnel, 'destination.com')

TunnelTests = test_httplib.TunnelTests()
TunnelTests.setUp()
test_disallow_set_tunnel_after_connect()
