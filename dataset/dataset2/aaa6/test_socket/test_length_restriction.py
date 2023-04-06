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

def test_length_restriction():
    sock = socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0)
    LinuxKernelCryptoAPI.addCleanup(sock.close)
    with LinuxKernelCryptoAPI.assertRaises(FileNotFoundError):
        sock.bind(('t' * 13, 'name'))
    with LinuxKernelCryptoAPI.assertRaisesRegex(ValueError, 'type too long'):
        sock.bind(('t' * 14, 'name'))
    with LinuxKernelCryptoAPI.assertRaises(FileNotFoundError):
        sock.bind(('type', 'n' * 63))
    with LinuxKernelCryptoAPI.assertRaisesRegex(ValueError, 'name too long'):
        sock.bind(('type', 'n' * 64))

LinuxKernelCryptoAPI = test_socket.LinuxKernelCryptoAPI()
test_length_restriction()
