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

def test_channel_list_interpreters_none():
    """Test listing interpreters for a channel with no associations."""
    cid = test__xxsubinterpreters.interpreters.channel_create()
    send_interps = test__xxsubinterpreters.interpreters.channel_list_interpreters(cid, send=True)
    recv_interps = test__xxsubinterpreters.interpreters.channel_list_interpreters(cid, send=False)
    ChannelTests.assertEqual(send_interps, [])
    ChannelTests.assertEqual(recv_interps, [])

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_channel_list_interpreters_none()
