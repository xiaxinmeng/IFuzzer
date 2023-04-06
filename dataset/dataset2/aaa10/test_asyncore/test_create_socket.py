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

def test_create_socket():
    s = asyncore.dispatcher()
    s.create_socket(BaseTestAPI.family)
    BaseTestAPI.assertEqual(s.socket.type, socket.SOCK_STREAM)
    BaseTestAPI.assertEqual(s.socket.family, BaseTestAPI.family)
    BaseTestAPI.assertEqual(s.socket.gettimeout(), 0)
    BaseTestAPI.assertFalse(s.socket.get_inheritable())

BaseTestAPI = test_asyncore.BaseTestAPI()
test_create_socket()
