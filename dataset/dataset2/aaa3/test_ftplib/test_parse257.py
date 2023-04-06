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

def test_parse257():
    TestFTPClass.assertEqual(ftplib.parse257('257 "/foo/bar"'), '/foo/bar')
    TestFTPClass.assertEqual(ftplib.parse257('257 "/foo/bar" created'), '/foo/bar')
    TestFTPClass.assertEqual(ftplib.parse257('257 ""'), '')
    TestFTPClass.assertEqual(ftplib.parse257('257 "" created'), '')
    TestFTPClass.assertRaises(ftplib.error_reply, ftplib.parse257, '250 "/foo/bar"')
    TestFTPClass.assertEqual(ftplib.parse257('257 "/foo/b""ar"'), '/foo/b"ar')
    TestFTPClass.assertEqual(ftplib.parse257('257 "/foo/b""ar" created'), '/foo/b"ar')

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_parse257()
