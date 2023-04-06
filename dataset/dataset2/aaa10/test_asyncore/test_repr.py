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

def test_repr():
    d = asyncore.dispatcher()
    DispatcherTests.assertEqual(repr(d), '<asyncore.dispatcher at %#x>' % id(d))

DispatcherTests = test_asyncore.DispatcherTests()
test_repr()
