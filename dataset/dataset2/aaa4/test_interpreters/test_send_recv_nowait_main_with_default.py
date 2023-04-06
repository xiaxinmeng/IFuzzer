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

def test_send_recv_nowait_main_with_default():
    (r, _) = interpreters.create_channel()
    obj = r.recv_nowait(None)
    TestSendRecv.assertIsNone(obj)

TestSendRecv = test_interpreters.TestSendRecv()
test_send_recv_nowait_main_with_default()
