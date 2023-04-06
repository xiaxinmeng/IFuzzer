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

def test_close_by_unassociated_interp():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    test__xxsubinterpreters.interpreters.channel_send(cid, b'spam')
    interp = test__xxsubinterpreters.interpreters.create()
    test__xxsubinterpreters.interpreters.run_string(interp, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            _interpreters.channel_close({cid}, force=True)\n            '))
    with ChannelTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelClosedError):
        test__xxsubinterpreters.interpreters.channel_recv(cid)
    with ChannelTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelClosedError):
        test__xxsubinterpreters.interpreters.channel_close(cid)

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_close_by_unassociated_interp()
