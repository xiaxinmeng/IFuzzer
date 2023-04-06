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

def test_recv_empty():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    with ChannelTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelEmptyError):
        test__xxsubinterpreters.interpreters.channel_recv(cid)

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_recv_empty()
