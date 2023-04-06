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

@unittest.skipIf(sys.platform.startswith('sunos'), 'OOB support is broken on Solaris')
def test_handle_expt():
    if test_asyncore.HAS_UNIX_SOCKETS and BaseTestAPI.family == socket.AF_UNIX:
        BaseTestAPI.skipTest('Not applicable to AF_UNIX sockets.')
    if sys.platform == 'darwin' and BaseTestAPI.use_poll:
        BaseTestAPI.skipTest('poll may fail on macOS; see issue #28087')

    class TestClient(test_asyncore.BaseClient):

        def handle_expt(BaseTestAPI):
            BaseTestAPI.socket.recv(1024, socket.MSG_OOB)
            BaseTestAPI.flag = True

    class TestHandler(BaseTestHandler):

        def __init__(BaseTestAPI, conn):
            BaseTestHandler.__init__(BaseTestAPI, conn)
            BaseTestAPI.socket.send(bytes(chr(244), 'latin-1'), socket.MSG_OOB)
    server = test_asyncore.BaseServer(BaseTestAPI.family, BaseTestAPI.addr, TestHandler)
    client = TestClient(BaseTestAPI.family, server.address)
    BaseTestAPI.loop_waiting_for_flag(client)

BaseTestAPI = test_asyncore.BaseTestAPI()
test_handle_expt()
