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

def test_default_kwargs():
    cid = test__xxsubinterpreters.interpreters._channel_id(10, force=True)
    ChannelIDTests.assertEqual(int(cid), 10)
    ChannelIDTests.assertEqual(cid.end, 'both')

ChannelIDTests = test__xxsubinterpreters.ChannelIDTests()
test_default_kwargs()
