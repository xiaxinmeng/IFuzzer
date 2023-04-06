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

def test_makeport():
    with TestFTPClass.client.makeport():
        TestFTPClass.assertEqual(TestFTPClass.server.handler_instance.last_received_cmd, 'eprt')

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_makeport()
