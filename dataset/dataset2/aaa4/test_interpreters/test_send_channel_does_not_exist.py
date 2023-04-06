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

def test_send_channel_does_not_exist():
    ch = interpreters.SendChannel(1000000)
    with TestSendRecv.assertRaises(interpreters.ChannelNotFoundError):
        ch.send(b'spam')

TestSendRecv = test_interpreters.TestSendRecv()
test_send_channel_does_not_exist()
