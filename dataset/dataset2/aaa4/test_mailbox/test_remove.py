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

def test_remove():
    TestMailbox._test_remove_or_delitem(TestMailbox._box.remove)

TestMailbox = test_mailbox.TestMailbox()
TestMailbox.setUp()
test_remove()
