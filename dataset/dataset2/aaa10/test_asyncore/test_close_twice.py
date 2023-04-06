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

def test_close_twice():
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    f = asyncore.file_wrapper(fd)
    os.close(fd)
    os.close(f.fd)
    with FileWrapperTest.assertRaises(OSError):
        f.close()
    FileWrapperTest.assertEqual(f.fd, -1)
    f.close()

FileWrapperTest = test_asyncore.FileWrapperTest()
test_close_twice()
