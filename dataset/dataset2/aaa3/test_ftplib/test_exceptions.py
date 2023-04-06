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

def test_exceptions():
    TestFTPClass.assertRaises(ValueError, TestFTPClass.client.sendcmd, 'echo 40\r\n0')
    TestFTPClass.assertRaises(ValueError, TestFTPClass.client.sendcmd, 'echo 40\n0')
    TestFTPClass.assertRaises(ValueError, TestFTPClass.client.sendcmd, 'echo 40\r0')
    TestFTPClass.assertRaises(ftplib.error_temp, TestFTPClass.client.sendcmd, 'echo 400')
    TestFTPClass.assertRaises(ftplib.error_temp, TestFTPClass.client.sendcmd, 'echo 499')
    TestFTPClass.assertRaises(ftplib.error_perm, TestFTPClass.client.sendcmd, 'echo 500')
    TestFTPClass.assertRaises(ftplib.error_perm, TestFTPClass.client.sendcmd, 'echo 599')
    TestFTPClass.assertRaises(ftplib.error_proto, TestFTPClass.client.sendcmd, 'echo 999')

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_exceptions()
