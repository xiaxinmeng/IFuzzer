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

def test_transfer():

    def retr():

        def callback(data):
            received.append(data.decode(TestIPv6Environment.client.encoding))
        received = []
        TestIPv6Environment.client.retrbinary('retr', callback)
        TestIPv6Environment.assertEqual(len(''.join(received)), len(test_ftplib.RETR_DATA))
        TestIPv6Environment.assertEqual(''.join(received), test_ftplib.RETR_DATA)
    TestIPv6Environment.client.set_pasv(True)
    retr()
    TestIPv6Environment.client.set_pasv(False)
    retr()

TestIPv6Environment = test_ftplib.TestIPv6Environment()
TestIPv6Environment.setUp()
test_transfer()
