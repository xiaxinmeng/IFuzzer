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

def test_makepasv():
    (host, port) = TestFTPClass.client.makepasv()
    conn = socket.create_connection((host, port), timeout=test_ftplib.TIMEOUT)
    conn.close()
    TestFTPClass.assertEqual(TestFTPClass.server.handler_instance.last_received_cmd, 'epsv')

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_makepasv()
