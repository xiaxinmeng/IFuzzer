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

def test_context_manager():
    with socketserver.TCPServer((test_socketserver.HOST, 0), socketserver.StreamRequestHandler) as server:
        pass
    SocketServerTest.assertEqual(-1, server.socket.fileno())

SocketServerTest = test_socketserver.SocketServerTest()
test_context_manager()
