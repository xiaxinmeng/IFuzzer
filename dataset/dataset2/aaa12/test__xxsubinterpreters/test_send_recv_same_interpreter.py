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

def test_send_recv_same_interpreter():
    id1 = test__xxsubinterpreters.interpreters.create()
    out = test__xxsubinterpreters._run_output(id1, dedent("\n            import _xxsubinterpreters as _interpreters\n            cid = _interpreters.channel_create()\n            orig = b'spam'\n            _interpreters.channel_send(cid, orig)\n            obj = _interpreters.channel_recv(cid)\n            assert obj is not orig\n            assert obj == orig\n            "))

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_send_recv_same_interpreter()
