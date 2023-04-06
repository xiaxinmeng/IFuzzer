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

def test_ThreadingTCPServer():
    SocketServerTest.run_server(socketserver.ThreadingTCPServer, socketserver.StreamRequestHandler, SocketServerTest.stream_examine)

SocketServerTest = test_socketserver.SocketServerTest()
test_ThreadingTCPServer()
