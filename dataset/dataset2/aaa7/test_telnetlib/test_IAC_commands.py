import socket
import selectors
import telnetlib
import threading
import contextlib
from test import support
from test.support import socket_helper
import unittest
import test_telnetlib

def test_IAC_commands():
    for cmd in OptionTests.cmds:
        OptionTests._test_command([test_telnetlib.tl.IAC, cmd])
        OptionTests._test_command([b'x' * 100, test_telnetlib.tl.IAC, cmd, b'y' * 100])
        OptionTests._test_command([b'x' * 10, test_telnetlib.tl.IAC, cmd, b'y' * 10])
    OptionTests._test_command([test_telnetlib.tl.IAC + cmd for cmd in OptionTests.cmds])

OptionTests = test_telnetlib.OptionTests()
test_IAC_commands()
