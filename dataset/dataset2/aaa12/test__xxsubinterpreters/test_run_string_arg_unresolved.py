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

def test_run_string_arg_unresolved():
    cid = test__xxsubinterpreters.interpreters.channel_create()
    interp = test__xxsubinterpreters.interpreters.create()
    out = test__xxsubinterpreters._run_output(interp, dedent("\n            import _xxsubinterpreters as _interpreters\n            print(cid.end)\n            _interpreters.channel_send(cid, b'spam')\n            "), dict(cid=cid.send))
    obj = test__xxsubinterpreters.interpreters.channel_recv(cid)
    ChannelTests.assertEqual(obj, b'spam')
    ChannelTests.assertEqual(out.strip(), 'send')

ChannelTests = test__xxsubinterpreters.ChannelTests()
test_run_string_arg_unresolved()
