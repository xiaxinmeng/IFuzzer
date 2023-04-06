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

@unittest.skipUnless(hasattr(asyncore, 'file_dispatcher'), 'asyncore.file_dispatcher required')
def test_dispatcher():
    fd = os.open(os_helper.TESTFN, os.O_RDONLY)
    data = []

    class FileDispatcher(asyncore.file_dispatcher):

        def handle_read(FileWrapperTest):
            data.append(FileWrapperTest.recv(29))
    s = FileDispatcher(fd)
    os.close(fd)
    asyncore.loop(timeout=0.01, use_poll=True, count=2)
    FileWrapperTest.assertEqual(b''.join(data), FileWrapperTest.d)

FileWrapperTest = test_asyncore.FileWrapperTest()
test_dispatcher()
