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

def test_connection_attributes():
    server = test_asyncore.BaseServer(BaseTestAPI.family, BaseTestAPI.addr)
    client = test_asyncore.BaseClient(BaseTestAPI.family, server.address)
    BaseTestAPI.assertFalse(server.connected)
    BaseTestAPI.assertTrue(server.accepting)
    BaseTestAPI.assertFalse(client.accepting)
    asyncore.loop(timeout=0.01, use_poll=BaseTestAPI.use_poll, count=100)
    BaseTestAPI.assertFalse(server.connected)
    BaseTestAPI.assertTrue(server.accepting)
    BaseTestAPI.assertTrue(client.connected)
    BaseTestAPI.assertFalse(client.accepting)
    client.close()
    BaseTestAPI.assertFalse(server.connected)
    BaseTestAPI.assertTrue(server.accepting)
    BaseTestAPI.assertFalse(client.connected)
    BaseTestAPI.assertFalse(client.accepting)
    server.close()
    BaseTestAPI.assertFalse(server.connected)
    BaseTestAPI.assertFalse(server.accepting)

BaseTestAPI = test_asyncore.BaseTestAPI()
test_connection_attributes()
