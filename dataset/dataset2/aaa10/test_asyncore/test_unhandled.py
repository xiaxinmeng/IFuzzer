import asyncore
import unittest
import select
import os
import socket
import sys
import time
import errno
import struct
import threading
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import threading_helper
from test.support import warnings_helper
from io import BytesIO
import test_asyncore

def test_unhandled():
    d = asyncore.dispatcher()
    d.ignore_log_types = ()
    with support.captured_stdout() as stdout:
        d.handle_expt()
        d.handle_read()
        d.handle_write()
        d.handle_connect()
    lines = stdout.getvalue().splitlines()
    expected = ['warning: unhandled incoming priority event', 'warning: unhandled read event', 'warning: unhandled write event', 'warning: unhandled connect event']
    DispatcherTests.assertEqual(lines, expected)

DispatcherTests = test_asyncore.DispatcherTests()
test_unhandled()
