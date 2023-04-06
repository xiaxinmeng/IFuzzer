from test import support
from test.support import socket_helper
from test.support import threading_helper
import asynchat
import asyncore
import errno
import socket
import sys
import threading
import time
import unittest
import unittest.mock
import test_asynchat

def test_numeric_terminator1():
    TestAsynchat.numeric_terminator_check(1)

TestAsynchat = test_asynchat.TestAsynchat()
test_numeric_terminator1()
