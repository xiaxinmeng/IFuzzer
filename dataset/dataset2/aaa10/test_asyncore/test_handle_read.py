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

def test_handle_read():

    class TestClient(test_asyncore.BaseClient):

        def handle_read(BaseTestAPI):
            BaseTestAPI.flag = True

    class TestHandler(test_asyncore.BaseTestHandler):

        def __init__(BaseTestAPI, conn):
            BaseTestHandler.__init__(BaseTestAPI, conn)
            BaseTestAPI.send(b'x' * 1024)
    server = test_asyncore.BaseServer(BaseTestAPI.family, BaseTestAPI.addr, TestHandler)
    client = TestClient(BaseTestAPI.family, server.address)
    BaseTestAPI.loop_waiting_for_flag(client)

BaseTestAPI = test_asyncore.BaseTestAPI()
test_handle_read()
