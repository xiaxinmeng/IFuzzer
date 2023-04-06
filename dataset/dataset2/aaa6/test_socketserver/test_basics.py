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

def test_basics():

    class Handler(socketserver.StreamRequestHandler):

        def handle(SocketWriterTest):
            SocketWriterTest.server.wfile = SocketWriterTest.wfile
            SocketWriterTest.server.wfile_fileno = SocketWriterTest.wfile.fileno()
            SocketWriterTest.server.request_fileno = SocketWriterTest.request.fileno()
    server = socketserver.TCPServer((test_socketserver.HOST, 0), Handler)
    SocketWriterTest.addCleanup(server.server_close)
    s = socket.socket(server.address_family, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    with s:
        s.connect(server.server_address)
    server.handle_request()
    SocketWriterTest.assertIsInstance(server.wfile, io.BufferedIOBase)
    SocketWriterTest.assertEqual(server.wfile_fileno, server.request_fileno)

SocketWriterTest = test_socketserver.SocketWriterTest()
test_basics()
