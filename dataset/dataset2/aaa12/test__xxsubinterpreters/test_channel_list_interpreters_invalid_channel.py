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

def test_channel_list_interpreters_invalid_channel():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    with ChannelTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelNotFoundError):
        test__xxsubinterpreters.interpreters.channel_list_interpreters(1000, send=True)
    test__xxsubinterpreters.interpreters.channel_close(cid)
    with ChannelTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelClosedError):
        test__xxsubinterpreters.interpreters.channel_list_interpreters(cid, send=True)

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_channel_list_interpreters_invalid_channel()
