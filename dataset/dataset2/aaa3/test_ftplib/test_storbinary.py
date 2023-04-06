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

def test_storbinary():
    f = io.BytesIO(test_ftplib.RETR_DATA.encode(TestFTPClass.client.encoding))
    TestFTPClass.client.storbinary('stor', f)
    TestFTPClass.check_data(TestFTPClass.server.handler_instance.last_received_data, test_ftplib.RETR_DATA)
    flag = []
    f.seek(0)
    TestFTPClass.client.storbinary('stor', f, callback=lambda x: flag.append(None))
    TestFTPClass.assertTrue(flag)

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_storbinary()
