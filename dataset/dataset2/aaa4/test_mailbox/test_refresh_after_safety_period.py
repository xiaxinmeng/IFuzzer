import os
import sys
import time
import stat
import socket
import email
import email.message
import re
import io
import tempfile
from test import support
from test.support import os_helper
import unittest
import textwrap
import mailbox
import glob
import test_mailbox

def test_refresh_after_safety_period():
    key0 = TestMaildir._box.add(TestMaildir._template % 0)
    key1 = TestMaildir._box.add(TestMaildir._template % 1)
    TestMaildir._box = TestMaildir._factory(TestMaildir._path)
    TestMaildir.assertEqual(TestMaildir._box._toc, {})
    TestMaildir._box._skewfactor = -3
    TestMaildir._box._refresh()
    TestMaildir.assertEqual(sorted(TestMaildir._box._toc.keys()), sorted([key0, key1]))

TestMaildir = test_mailbox.TestMaildir()
TestMaildir.setUp()
test_refresh_after_safety_period()
