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

def test_message_separator():
    TestMbox._box.add('From: foo\n\n0')
    with open(TestMbox._path) as f:
        data = f.read()
        TestMbox.assertEqual(data[-3:], '0\n\n')
    TestMbox._box.add('From: foo\n\n0\n')
    with open(TestMbox._path) as f:
        data = f.read()
        TestMbox.assertEqual(data[-3:], '0\n\n')

TestMbox = test_mailbox.TestMbox()
TestMbox.setUp()
test_message_separator()
