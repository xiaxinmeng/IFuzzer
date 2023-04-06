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

def test_used_multiple_times_by_single_user():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    test__xxsubinterpreters.interpreters.channel_send(cid, b'spam')
    test__xxsubinterpreters.interpreters.channel_send(cid, b'spam')
    test__xxsubinterpreters.interpreters.channel_send(cid, b'spam')
    test__xxsubinterpreters.interpreters.channel_recv(cid)
    test__xxsubinterpreters.interpreters.channel_release(cid, send=True, recv=True)
    with ChannelReleaseTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelClosedError):
        test__xxsubinterpreters.interpreters.channel_send(cid, b'eggs')
    with ChannelReleaseTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelClosedError):
        test__xxsubinterpreters.interpreters.channel_recv(cid)

ChannelReleaseTests = test__xxsubinterpreters.ChannelReleaseTests()
test_used_multiple_times_by_single_user()
