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

def test_data_connection():
    with TestTLS_FTPClass.client.transfercmd('list') as sock:
        TestTLS_FTPClass.assertNotIsInstance(sock, ssl.SSLSocket)
        TestTLS_FTPClass.assertEqual(sock.recv(1024), test_ftplib.LIST_DATA.encode(TestTLS_FTPClass.client.encoding))
    TestTLS_FTPClass.assertEqual(TestTLS_FTPClass.client.voidresp(), '226 transfer complete')
    TestTLS_FTPClass.client.prot_p()
    with TestTLS_FTPClass.client.transfercmd('list') as sock:
        TestTLS_FTPClass.assertIsInstance(sock, ssl.SSLSocket)
        TestTLS_FTPClass.assertEqual(sock.recv(1024), LIST_DATA.encode(TestTLS_FTPClass.client.encoding))
    TestTLS_FTPClass.assertEqual(TestTLS_FTPClass.client.voidresp(), '226 transfer complete')
    TestTLS_FTPClass.client.prot_c()
    with TestTLS_FTPClass.client.transfercmd('list') as sock:
        TestTLS_FTPClass.assertNotIsInstance(sock, ssl.SSLSocket)
        TestTLS_FTPClass.assertEqual(sock.recv(1024), LIST_DATA.encode(TestTLS_FTPClass.client.encoding))
    TestTLS_FTPClass.assertEqual(TestTLS_FTPClass.client.voidresp(), '226 transfer complete')

TestTLS_FTPClass = test_ftplib.TestTLS_FTPClass()
TestTLS_FTPClass.setUp()
test_data_connection()
