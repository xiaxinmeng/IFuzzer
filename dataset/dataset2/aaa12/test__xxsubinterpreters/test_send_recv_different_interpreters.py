from collections import namedtuple
import contextlib
import itertools
import os
import pickle
import sys
from textwrap import dedent
import threading
import time
import unittest
from test import support
from test.support import import_helper
from test.support import script_helper
import tempfile
import test__xxsubinterpreters

def test_send_recv_different_interpreters():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    id1 = test__xxsubinterpreters.interpreters.create()
    out = test__xxsubinterpreters._run_output(id1, dedent(f"\n            import _xxsubinterpreters as _interpreters\n            _interpreters.channel_send({cid}, b'spam')\n            "))
    obj = test__xxsubinterpreters.interpreters.channel_recv(cid)
    ChannelTests.assertEqual(obj, b'spam')

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_send_recv_different_interpreters()
