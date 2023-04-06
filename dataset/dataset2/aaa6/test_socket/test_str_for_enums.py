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

def test_str_for_enums():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        GeneralModuleTests.assertEqual(str(s.family), 'AddressFamily.AF_INET')
        GeneralModuleTests.assertEqual(str(s.type), 'SocketKind.SOCK_STREAM')

GeneralModuleTests = test_socket.GeneralModuleTests()
test_str_for_enums()
