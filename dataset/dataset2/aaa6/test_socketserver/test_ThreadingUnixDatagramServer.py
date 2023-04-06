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

@test_socketserver.requires_unix_sockets
def test_ThreadingUnixDatagramServer():
    SocketServerTest.run_server(socketserver.ThreadingUnixDatagramServer, socketserver.DatagramRequestHandler, SocketServerTest.dgram_examine)

SocketServerTest = test_socketserver.SocketServerTest()
SocketServerTest.setUp()
test_ThreadingUnixDatagramServer()
