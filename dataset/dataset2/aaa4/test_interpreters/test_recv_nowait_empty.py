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

def test_recv_nowait_empty():
    (ch, _) = interpreters.create_channel()
    with TestSendRecv.assertRaises(interpreters.ChannelEmptyError):
        ch.recv_nowait()

TestSendRecv = test_interpreters.TestSendRecv()
test_recv_nowait_empty()
