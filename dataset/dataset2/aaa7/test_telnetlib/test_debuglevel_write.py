import socket
import selectors
import telnetlib
import threading
import contextlib
from test import support
from test.support import socket_helper
import unittest
import test_telnetlib

def test_debuglevel_write():
    telnet = test_telnetlib.test_telnet()
    telnet.set_debuglevel(1)
    telnet.write(b'xxx')
    expected = "send b'xxx'\n"
    OptionTests.assertIn(expected, telnet._messages)

OptionTests = test_telnetlib.OptionTests()
test_debuglevel_write()
