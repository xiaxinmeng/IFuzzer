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

def test_voidcmd():
    TestFTPClass.client.voidcmd('echo 200')
    TestFTPClass.client.voidcmd('echo 299')
    TestFTPClass.assertRaises(ftplib.error_reply, TestFTPClass.client.voidcmd, 'echo 199')
    TestFTPClass.assertRaises(ftplib.error_reply, TestFTPClass.client.voidcmd, 'echo 300')

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_voidcmd()
