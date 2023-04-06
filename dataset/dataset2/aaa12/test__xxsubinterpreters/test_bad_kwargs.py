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

def test_bad_kwargs():
    with ChannelIDTests.assertRaises(ValueError):
        test__xxsubinterpreters.interpreters._channel_id(10, send=False, recv=False)

ChannelIDTests = test__xxsubinterpreters.ChannelIDTests()
test_bad_kwargs()
