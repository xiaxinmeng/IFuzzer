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

def test_source_address_passive_connection():
    port = socket_helper.find_unused_port()
    TestFTPClass.client.source_address = (HOST, port)
    try:
        with TestFTPClass.client.transfercmd('list') as sock:
            TestFTPClass.assertEqual(sock.getsockname()[1], port)
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            TestFTPClass.skipTest("couldn't bind to port %d" % port)
        raise

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_source_address_passive_connection()
