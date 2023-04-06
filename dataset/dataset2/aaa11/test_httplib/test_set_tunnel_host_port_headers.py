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

def test_set_tunnel_host_port_headers():
    tunnel_host = 'destination.com'
    tunnel_port = 8888
    tunnel_headers = {'User-Agent': 'Mozilla/5.0 (compatible, MSIE 11)'}
    TunnelTests.conn.set_tunnel(tunnel_host, port=tunnel_port, headers=tunnel_headers)
    TunnelTests.conn.request('HEAD', '/', '')
    TunnelTests.assertEqual(TunnelTests.conn.sock.host, TunnelTests.host)
    TunnelTests.assertEqual(TunnelTests.conn.sock.port, client.HTTP_PORT)
    TunnelTests.assertEqual(TunnelTests.conn._tunnel_host, tunnel_host)
    TunnelTests.assertEqual(TunnelTests.conn._tunnel_port, tunnel_port)
    TunnelTests.assertEqual(TunnelTests.conn._tunnel_headers, tunnel_headers)

TunnelTests = test_httplib.TunnelTests()
TunnelTests.setUp()
test_set_tunnel_host_port_headers()
