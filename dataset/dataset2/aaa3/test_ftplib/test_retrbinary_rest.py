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

def test_retrbinary_rest():

    def callback(data):
        received.append(data.decode(TestFTPClass.client.encoding))
    for rest in (0, 10, 20):
        received = []
        TestFTPClass.client.retrbinary('retr', callback, rest=rest)
        TestFTPClass.check_data(''.join(received), test_ftplib.RETR_DATA[rest:])

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_retrbinary_rest()
