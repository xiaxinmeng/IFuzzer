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

def test_recv_channel_does_not_exist():
    ch = interpreters.RecvChannel(1000000)
    with TestSendRecv.assertRaises(interpreters.ChannelNotFoundError):
        ch.recv()

TestSendRecv = test_interpreters.TestSendRecv()
test_recv_channel_does_not_exist()
