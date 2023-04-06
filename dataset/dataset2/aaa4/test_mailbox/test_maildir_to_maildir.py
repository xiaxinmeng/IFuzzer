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

def test_maildir_to_maildir():
    msg_maildir = mailbox.MaildirMessage(test_mailbox._sample_message)
    msg_maildir.set_flags('DFPRST')
    msg_maildir.set_subdir('cur')
    date = msg_maildir.get_date()
    msg = mailbox.MaildirMessage(msg_maildir)
    TestMessageConversion._check_sample(msg)
    TestMessageConversion.assertEqual(msg.get_flags(), 'DFPRST')
    TestMessageConversion.assertEqual(msg.get_subdir(), 'cur')
    TestMessageConversion.assertEqual(msg.get_date(), date)

TestMessageConversion = test_mailbox.TestMessageConversion()
test_maildir_to_maildir()
