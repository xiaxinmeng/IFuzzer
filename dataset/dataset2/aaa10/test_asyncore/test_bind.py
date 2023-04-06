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

def test_bind():
    if test_asyncore.HAS_UNIX_SOCKETS and BaseTestAPI.family == socket.AF_UNIX:
        BaseTestAPI.skipTest('Not applicable to AF_UNIX sockets.')
    s1 = asyncore.dispatcher()
    s1.create_socket(BaseTestAPI.family)
    s1.bind(BaseTestAPI.addr)
    s1.listen(5)
    port = s1.socket.getsockname()[1]
    s2 = asyncore.dispatcher()
    s2.create_socket(BaseTestAPI.family)
    BaseTestAPI.assertRaises(OSError, s2.bind, (BaseTestAPI.addr[0], port))

BaseTestAPI = test_asyncore.BaseTestAPI()
test_bind()
