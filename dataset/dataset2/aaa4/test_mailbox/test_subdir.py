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

def test_subdir():
    msg = mailbox.MaildirMessage(test_mailbox._sample_message)
    TestMaildirMessage.assertEqual(msg.get_subdir(), 'new')
    msg.set_subdir('cur')
    TestMaildirMessage.assertEqual(msg.get_subdir(), 'cur')
    msg.set_subdir('new')
    TestMaildirMessage.assertEqual(msg.get_subdir(), 'new')
    TestMaildirMessage.assertRaises(ValueError, lambda : msg.set_subdir('tmp'))
    TestMaildirMessage.assertEqual(msg.get_subdir(), 'new')
    msg.set_subdir('new')
    TestMaildirMessage.assertEqual(msg.get_subdir(), 'new')
    TestMaildirMessage._check_sample(msg)

TestMaildirMessage = test_mailbox.TestMaildirMessage()
test_subdir()
