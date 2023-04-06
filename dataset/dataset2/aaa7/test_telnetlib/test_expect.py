import socket
import selectors
import telnetlib
import threading
import contextlib
from test import support
from test.support import socket_helper
import unittest
import test_telnetlib

def test_expect():
    """
        expect(expected, [timeout])
          Read until the expected string has been seen, or a timeout is
          hit (default is no timeout); may block.
        """
    want = [b'x' * 10, b'match', b'y' * 10]
    telnet = test_telnetlib.test_telnet(want)
    (_, _, data) = telnet.expect([b'match'])
    ExpectTests.assertEqual(data, b''.join(want[:-1]))

ExpectTests = test_telnetlib.ExpectTests()
test_expect()
