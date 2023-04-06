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

def test_handle_accept():

    class TestListener(test_asyncore.BaseTestHandler):

        def __init__(BaseTestAPI, family, addr):
            BaseTestHandler.__init__(BaseTestAPI)
            BaseTestAPI.create_socket(family)
            bind_af_aware(BaseTestAPI.socket, addr)
            BaseTestAPI.listen(5)
            BaseTestAPI.address = BaseTestAPI.socket.getsockname()

        def handle_accept(BaseTestAPI):
            BaseTestAPI.flag = True
    server = TestListener(BaseTestAPI.family, BaseTestAPI.addr)
    client = BaseClient(BaseTestAPI.family, server.address)
    BaseTestAPI.loop_waiting_for_flag(server)

BaseTestAPI = test_asyncore.BaseTestAPI()
test_handle_accept()
