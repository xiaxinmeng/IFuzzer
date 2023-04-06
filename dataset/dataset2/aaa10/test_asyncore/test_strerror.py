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

def test_strerror():
    err = asyncore._strerror(errno.EPERM)
    if hasattr(os, 'strerror'):
        DispatcherTests.assertEqual(err, os.strerror(errno.EPERM))
    err = asyncore._strerror(-1)
    DispatcherTests.assertTrue(err != '')

DispatcherTests = test_asyncore.DispatcherTests()
test_strerror()
