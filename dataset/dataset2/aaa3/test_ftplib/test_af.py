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

def test_af():
    TestIPv6Environment.assertEqual(TestIPv6Environment.client.af, socket.AF_INET6)

TestIPv6Environment = test_ftplib.TestIPv6Environment()
TestIPv6Environment.setUp()
test_af()
