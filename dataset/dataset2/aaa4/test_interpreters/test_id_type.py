import contextlib
import os
import threading
from textwrap import dedent
import unittest
import time
import _xxsubinterpreters as _interpreters
from test.support import interpreters
import tempfile
import test_interpreters

def test_id_type():
    (_, sch) = interpreters.create_channel()
    TestInterpreterAttrs.assertIsInstance(sch.id, _interpreters.ChannelID)

TestInterpreterAttrs = test_interpreters.TestInterpreterAttrs()
test_id_type()
