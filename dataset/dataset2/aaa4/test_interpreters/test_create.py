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

def test_create():
    (r, s) = interpreters.create_channel()
    TestChannels.assertIsInstance(r, interpreters.RecvChannel)
    TestChannels.assertIsInstance(s, interpreters.SendChannel)

TestChannels = test_interpreters.TestChannels()
test_create()
