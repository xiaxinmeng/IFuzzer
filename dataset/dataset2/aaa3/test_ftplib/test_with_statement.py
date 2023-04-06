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

def test_with_statement():
    TestFTPClass.client.quit()

    def is_client_connected():
        if TestFTPClass.client.sock is None:
            return False
        try:
            TestFTPClass.client.sendcmd('noop')
        except (OSError, EOFError):
            return False
        return True
    with ftplib.FTP(timeout=test_ftplib.TIMEOUT) as TestFTPClass.client:
        TestFTPClass.client.connect(TestFTPClass.server.host, TestFTPClass.server.port)
        TestFTPClass.client.sendcmd('noop')
        TestFTPClass.assertTrue(is_client_connected())
    TestFTPClass.assertEqual(TestFTPClass.server.handler_instance.last_received_cmd, 'quit')
    TestFTPClass.assertFalse(is_client_connected())
    with ftplib.FTP(timeout=test_ftplib.TIMEOUT) as TestFTPClass.client:
        TestFTPClass.client.connect(TestFTPClass.server.host, TestFTPClass.server.port)
        TestFTPClass.client.sendcmd('noop')
        TestFTPClass.client.quit()
    TestFTPClass.assertEqual(TestFTPClass.server.handler_instance.last_received_cmd, 'quit')
    TestFTPClass.assertFalse(is_client_connected())
    try:
        with ftplib.FTP(timeout=test_ftplib.TIMEOUT) as TestFTPClass.client:
            TestFTPClass.client.connect(TestFTPClass.server.host, TestFTPClass.server.port)
            TestFTPClass.client.sendcmd('noop')
            TestFTPClass.server.handler_instance.next_response = '550 error on quit'
    except ftplib.error_perm as err:
        TestFTPClass.assertEqual(str(err), '550 error on quit')
    else:
        TestFTPClass.fail('Exception not raised')
    time.sleep(0.1)
    TestFTPClass.assertEqual(TestFTPClass.server.handler_instance.last_received_cmd, 'quit')
    TestFTPClass.assertFalse(is_client_connected())

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_with_statement()
