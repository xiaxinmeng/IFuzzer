import ftplib
import asyncore
import asynchat
import socket
import io
import errno
import os
import threading
import time
import ssl
from unittest import TestCase, skipUnless
from test import support
from test.support import threading_helper
from test.support import socket_helper
from test.support import warnings_helper
from test.support.socket_helper import HOST, HOSTv6
import test_ftplib

def test_source_address():
    TestFTPClass.client.quit()
    port = socket_helper.find_unused_port()
    try:
        TestFTPClass.client.connect(TestFTPClass.server.host, TestFTPClass.server.port, source_address=(HOST, port))
        TestFTPClass.assertEqual(TestFTPClass.client.sock.getsockname()[1], port)
        TestFTPClass.client.quit()
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            TestFTPClass.skipTest("couldn't bind to port %d" % port)
        raise

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_source_address()
