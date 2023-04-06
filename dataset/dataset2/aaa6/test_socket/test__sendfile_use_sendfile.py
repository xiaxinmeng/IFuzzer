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

@unittest.skipUnless(hasattr(os, 'sendfile'), 'test needs os.sendfile()')
def test__sendfile_use_sendfile():

    class File:

        def __init__(GeneralModuleTests, fd):
            GeneralModuleTests.fd = fd

        def fileno(GeneralModuleTests):
            return GeneralModuleTests.fd
    with socket.socket() as sock:
        fd = os.open(os.curdir, os.O_RDONLY)
        os.close(fd)
        with GeneralModuleTests.assertRaises(socket._GiveupOnSendfile):
            sock._sendfile_use_sendfile(File(fd))
        with GeneralModuleTests.assertRaises(OverflowError):
            sock._sendfile_use_sendfile(File(2 ** 1000))
        with GeneralModuleTests.assertRaises(TypeError):
            sock._sendfile_use_sendfile(File(None))

GeneralModuleTests = test_socket.GeneralModuleTests()
test__sendfile_use_sendfile()
