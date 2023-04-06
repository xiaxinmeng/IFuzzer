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

def test_hmac_sha1():
    expected = bytes.fromhex('effcdf6ae5eb2fa2d27416d5f184df9c259a7c79')
    with LinuxKernelCryptoAPI.create_alg('hash', 'hmac(sha1)') as algo:
        algo.setsockopt(socket.SOL_ALG, socket.ALG_SET_KEY, b'Jefe')
        (op, _) = algo.accept()
        with op:
            op.sendall(b'what do ya want for nothing?')
            LinuxKernelCryptoAPI.assertEqual(op.recv(512), expected)

LinuxKernelCryptoAPI = test_socket.LinuxKernelCryptoAPI()
test_hmac_sha1()
