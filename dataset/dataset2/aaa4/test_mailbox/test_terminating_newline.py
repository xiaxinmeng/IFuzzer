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

def test_terminating_newline():
    message = email.message.Message()
    message['From'] = 'john@example.com'
    message.set_payload('No newline at the end')
    i = TestMbox._box.add(message)
    message = TestMbox._box.get(i)
    TestMbox.assertEqual(message.get_payload(), 'No newline at the end\n')

TestMbox = test_mailbox.TestMbox()
TestMbox.setUp()
test_terminating_newline()
