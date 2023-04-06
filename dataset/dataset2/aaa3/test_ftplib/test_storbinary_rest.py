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

def test_storbinary_rest():
    data = test_ftplib.RETR_DATA.replace('\r\n', '\n').encode(TestFTPClass.client.encoding)
    f = io.BytesIO(data)
    for r in (30, '30'):
        f.seek(0)
        TestFTPClass.client.storbinary('stor', f, rest=r)
        TestFTPClass.assertEqual(TestFTPClass.server.handler_instance.rest, str(r))

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_storbinary_rest()
