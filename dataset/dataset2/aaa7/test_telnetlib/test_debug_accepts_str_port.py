import socket
import selectors
import telnetlib
import threading
import contextlib
from test import support
from test.support import socket_helper
import unittest
import test_telnetlib

def test_debug_accepts_str_port():
    with test_telnetlib.test_socket([]):
        telnet = test_telnetlib.TelnetAlike('dummy', '0')
        telnet._messages = ''
    telnet.set_debuglevel(1)
    telnet.msg('test')
    OptionTests.assertRegex(telnet._messages, '0.*test')

OptionTests = test_telnetlib.OptionTests()
test_debug_accepts_str_port()
