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

def test_singletons():
    for obj in [None]:
        with ShareableTypeTests.subTest(obj):
            test__xxsubinterpreters.interpreters.channel_send(ShareableTypeTests.cid, obj)
            got = test__xxsubinterpreters.interpreters.channel_recv(ShareableTypeTests.cid)
            ShareableTypeTests.assertIs(got, obj)

ShareableTypeTests = test__xxsubinterpreters.ShareableTypeTests()
ShareableTypeTests.setUp()
test_singletons()
