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

def test_all_errors():
    exceptions = (ftplib.error_reply, ftplib.error_temp, ftplib.error_perm, ftplib.error_proto, ftplib.Error, OSError, EOFError)
    for x in exceptions:
        try:
            raise x('exception not included in all_errors set')
        except ftplib.all_errors:
            pass

TestFTPClass = test_ftplib.TestFTPClass()
TestFTPClass.setUp()
test_all_errors()
