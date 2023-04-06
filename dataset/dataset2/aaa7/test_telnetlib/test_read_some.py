import socket
import selectors
import telnetlib
import threading
import contextlib
from test import support
from test.support import socket_helper
import unittest
import test_telnetlib

def test_read_some():
    """
        read_some()
          Read at least one byte or EOF; may block.
        """
    telnet = test_telnetlib.test_telnet([b'x' * 500])
    data = telnet.read_some()
    ReadTests.assertTrue(len(data) >= 1)
    telnet = test_telnetlib.test_telnet()
    data = telnet.read_some()
    ReadTests.assertEqual(b'', data)

ReadTests = test_telnetlib.ReadTests()
test_read_some()
