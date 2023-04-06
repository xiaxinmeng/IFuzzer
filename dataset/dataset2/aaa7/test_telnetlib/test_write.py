import socket
import selectors
import telnetlib
import threading
import contextlib
from test import support
from test.support import socket_helper
import unittest
import test_telnetlib

def test_write():
    data_sample = [b'data sample without IAC', b'data sample with' + test_telnetlib.tl.IAC + b' one IAC', b'a few' + test_telnetlib.tl.IAC + test_telnetlib.tl.IAC + b' iacs' + test_telnetlib.tl.IAC, test_telnetlib.tl.IAC, b'']
    for data in data_sample:
        telnet = test_telnetlib.test_telnet()
        telnet.write(data)
        written = b''.join(telnet.sock.writes)
        WriteTests.assertEqual(data.replace(test_telnetlib.tl.IAC, test_telnetlib.tl.IAC + test_telnetlib.tl.IAC), written)

WriteTests = test_telnetlib.WriteTests()
test_write()
