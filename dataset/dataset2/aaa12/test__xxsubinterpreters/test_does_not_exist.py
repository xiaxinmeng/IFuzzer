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

def test_does_not_exist():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    with IsRunningTests.assertRaises(test__xxsubinterpreters.interpreters.ChannelNotFoundError):
        test__xxsubinterpreters.interpreters._channel_id(int(cid) + 1)

IsRunningTests = test__xxsubinterpreters.IsRunningTests()
test_does_not_exist()
