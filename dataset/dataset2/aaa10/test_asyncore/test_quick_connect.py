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

@threading_helper.reap_threads
def test_quick_connect():
    if BaseTestAPI.family not in (socket.AF_INET, getattr(socket, 'AF_INET6', object())):
        BaseTestAPI.skipTest('test specific to AF_INET and AF_INET6')
    server = BaseServer(BaseTestAPI.family, BaseTestAPI.addr)
    t = threading.Thread(target=lambda : asyncore.loop(timeout=0.1, count=5))
    t.start()
    try:
        with socket.socket(BaseTestAPI.family, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
            try:
                s.connect(server.address)
            except OSError:
                pass
    finally:
        threading_helper.join_thread(t)

BaseTestAPI = test_asyncore.BaseTestAPI()
test_quick_connect()
