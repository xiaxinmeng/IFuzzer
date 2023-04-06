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

def test_with_kwargs():
    cid = test__xxsubinterpreters.interpreters._channel_id(10, send=True, force=True)
    ChannelIDTests.assertEqual(cid.end, 'send')
    cid = test__xxsubinterpreters.interpreters._channel_id(10, send=True, recv=False, force=True)
    ChannelIDTests.assertEqual(cid.end, 'send')
    cid = test__xxsubinterpreters.interpreters._channel_id(10, recv=True, force=True)
    ChannelIDTests.assertEqual(cid.end, 'recv')
    cid = test__xxsubinterpreters.interpreters._channel_id(10, recv=True, send=False, force=True)
    ChannelIDTests.assertEqual(cid.end, 'recv')
    cid = test__xxsubinterpreters.interpreters._channel_id(10, send=True, recv=True, force=True)
    ChannelIDTests.assertEqual(cid.end, 'both')

ChannelIDTests = test__xxsubinterpreters.ChannelIDTests()
test_with_kwargs()
