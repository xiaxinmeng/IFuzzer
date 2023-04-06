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

def test_unusable_closed_socketio():
    with socket.socket() as sock:
        fp = sock.makefile('rb', buffering=0)
        GeneralModuleTests.assertTrue(fp.readable())
        GeneralModuleTests.assertFalse(fp.writable())
        GeneralModuleTests.assertFalse(fp.seekable())
        fp.close()
        GeneralModuleTests.assertRaises(ValueError, fp.readable)
        GeneralModuleTests.assertRaises(ValueError, fp.writable)
        GeneralModuleTests.assertRaises(ValueError, fp.seekable)

GeneralModuleTests = test_socket.GeneralModuleTests()
test_unusable_closed_socketio()
