import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import threading_helper
import errno
import io
import itertools
import socket
import select
import tempfile
import time
import traceback
import queue
import sys
import os
import platform
import array
import contextlib
from weakref import proxy
import signal
import math
import pickle
import struct
import random
import shutil
import string
import _thread as thread
import threading
import multiprocessing
import fcntl
import _socket
import _socket
import _testcapi
from socket import inet_aton as f, inet_pton, AF_INET
from socket import inet_pton, AF_INET6, has_ipv6
from socket import inet_ntoa as f, inet_ntop, AF_INET
from socket import inet_ntop, AF_INET6, has_ipv6
import _testcapi
import _testcapi
import _testcapi
import _testcapi
import test_socket

@unittest.skipUnless(os.name == 'nt', 'Windows specific')
@unittest.skipUnless(hasattr(socket, 'SIO_LOOPBACK_FAST_PATH'), 'Loopback fast path support required for this test')
def test_sio_loopback_fast_path():
    s = socket.socket()
    GeneralModuleTests.addCleanup(s.close)
    try:
        s.ioctl(socket.SIO_LOOPBACK_FAST_PATH, True)
    except OSError as exc:
        WSAEOPNOTSUPP = 10045
        if exc.winerror == WSAEOPNOTSUPP:
            GeneralModuleTests.skipTest("SIO_LOOPBACK_FAST_PATH is defined but doesn't implemented in this Windows version")
        raise
    GeneralModuleTests.assertRaises(TypeError, s.ioctl, socket.SIO_LOOPBACK_FAST_PATH, None)

GeneralModuleTests = test_socket.GeneralModuleTests()
test_sio_loopback_fast_path()
