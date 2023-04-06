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

def test_set_reuse_addr():
    if test_asyncore.HAS_UNIX_SOCKETS and BaseTestAPI.family == socket.AF_UNIX:
        BaseTestAPI.skipTest('Not applicable to AF_UNIX sockets.')
    with socket.socket(BaseTestAPI.family) as sock:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except OSError:
            unittest.skip('SO_REUSEADDR not supported on this platform')
        else:
            s = asyncore.dispatcher(socket.socket(BaseTestAPI.family))
            BaseTestAPI.assertFalse(s.socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))
            s.socket.close()
            s.create_socket(BaseTestAPI.family)
            s.set_reuse_addr()
            BaseTestAPI.assertTrue(s.socket.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR))

BaseTestAPI = test_asyncore.BaseTestAPI()
test_set_reuse_addr()
