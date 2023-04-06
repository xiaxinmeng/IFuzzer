import socket
import selectors
import telnetlib
import threading
import contextlib
from test import support
from test.support import socket_helper
import unittest
import test_telnetlib

def test_read_eager():
    ReadTests._read_eager('read_eager')
    ReadTests._read_eager('read_very_eager')

ReadTests = test_telnetlib.ReadTests()
test_read_eager()
