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

def test_shutdown_request_called_if_verify_request_false():

    class MyServer(socketserver.TCPServer):

        def verify_request(MiscTestCase, request, client_address):
            return False
        shutdown_called = 0

        def shutdown_request(MiscTestCase, request):
            MiscTestCase.shutdown_called += 1
            socketserver.TCPServer.shutdown_request(MiscTestCase, request)
    server = MyServer((test_socketserver.HOST, 0), socketserver.StreamRequestHandler)
    s = socket.socket(server.address_family, socket.SOCK_STREAM)
    s.connect(server.server_address)
    s.close()
    server.handle_request()
    MiscTestCase.assertEqual(server.shutdown_called, 1)
    server.server_close()

MiscTestCase = test_socketserver.MiscTestCase()
test_shutdown_request_called_if_verify_request_false()
