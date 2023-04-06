import contextlib
import io
import os
import select
import signal
import socket
import tempfile
import threading
import unittest
import socketserver
import test.support
from test.support import reap_children, verbose
from test.support import os_helper
from test.support import socket_helper
from test.support import threading_helper
import test_socketserver

def test_tcpserver_bind_leak():
    for i in range(1024):
        with SocketServerTest.assertRaises(OverflowError):
            socketserver.TCPServer((test_socketserver.HOST, -1), socketserver.StreamRequestHandler)

SocketServerTest = test_socketserver.SocketServerTest()
test_tcpserver_bind_leak()
