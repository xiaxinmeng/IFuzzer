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

def test_list_all():
    TestChannels.assertEqual(interpreters.list_all_channels(), [])
    created = set()
    for _ in range(3):
        ch = interpreters.create_channel()
        created.add(ch)
    after = set(interpreters.list_all_channels())
    TestChannels.assertEqual(after, created)

TestChannels = test_interpreters.TestChannels()
test_list_all()
