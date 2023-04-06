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

def test_recv():
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    w = asyncore.file_wrapper(fd)
    os.close(fd)
    FileWrapperTest.assertNotEqual(w.fd, fd)
    FileWrapperTest.assertNotEqual(w.fileno(), fd)
    FileWrapperTest.assertEqual(w.recv(13), b"It's not dead")
    FileWrapperTest.assertEqual(w.read(6), b", it's")
    w.close()
    FileWrapperTest.assertRaises(OSError, w.read, 1)

FileWrapperTest = test_asyncore.FileWrapperTest()
test_recv()
