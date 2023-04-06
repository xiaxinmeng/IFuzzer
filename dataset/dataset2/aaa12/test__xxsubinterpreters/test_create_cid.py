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

def test_create_cid():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    ChannelTests.assertIsInstance(cid, test__xxsubinterpreters.interpreters.ChannelID)

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_create_cid()
