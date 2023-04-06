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

def test_popitem_and_flush_twice():
    TestMailbox._box.add(TestMailbox._template % 0)
    TestMailbox._box.add(TestMailbox._template % 1)
    TestMailbox._box.flush()
    TestMailbox._box.popitem()
    TestMailbox._box.flush()
    TestMailbox._box.popitem()
    TestMailbox._box.flush()

TestMailbox = test_mailbox.TestMailbox()
TestMailbox.setUp()
test_popitem_and_flush_twice()
