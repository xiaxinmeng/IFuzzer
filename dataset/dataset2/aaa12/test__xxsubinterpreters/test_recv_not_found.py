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

def test_recv_not_found():
    with ChannelTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelNotFoundError):
        test__xxsubinterpreters.interpreters.channel_recv(10)

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_recv_not_found()
