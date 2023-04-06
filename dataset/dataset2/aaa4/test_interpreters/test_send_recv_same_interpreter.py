import contextlib
import os
import threading
from textwrap import dedent
import unittest
import time
import _xxsubinterpreters as _interpreters
from test.support import interpreters
import tempfile
import test_interpreters

def test_send_recv_same_interpreter():
    interp = interpreters.create()
    interp.run(dedent("\n            from test.support import interpreters\n            r, s = interpreters.create_channel()\n            orig = b'spam'\n            s.send_nowait(orig)\n            obj = r.recv()\n            assert obj == orig, 'expected: obj == orig'\n            assert obj is not orig, 'expected: obj is not orig'\n            "))

TestSendRecv = test_interpreters.TestSendRecv()
test_send_recv_same_interpreter()
