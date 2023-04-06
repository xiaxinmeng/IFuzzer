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

def test_close_if_unassociated():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    interp = test__xxsubinterpreters.interpreters.create()
    test__xxsubinterpreters.interpreters.run_string(interp, dedent(f"\n            import _xxsubinterpreters as _interpreters\n            obj = _interpreters.channel_send({cid}, b'spam')\n            _interpreters.channel_release({cid})\n            "))
    with ChannelReleaseTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelClosedError):
        test__xxsubinterpreters.interpreters.channel_recv(cid)

ChannelReleaseTests = test__xxsubinterpreters.ChannelReleaseTests()
test_close_if_unassociated()
