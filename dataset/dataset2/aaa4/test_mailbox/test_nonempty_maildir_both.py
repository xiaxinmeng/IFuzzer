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

def test_nonempty_maildir_both():
    MaildirTestCase.createMessage('cur')
    MaildirTestCase.createMessage('new')
    MaildirTestCase.mbox = mailbox.Maildir(os_helper.TESTFN)
    MaildirTestCase.assertIsNotNone(MaildirTestCase.mbox.next())
    MaildirTestCase.assertIsNotNone(MaildirTestCase.mbox.next())
    MaildirTestCase.assertIsNone(MaildirTestCase.mbox.next())
    MaildirTestCase.assertIsNone(MaildirTestCase.mbox.next())

MaildirTestCase = test_mailbox.MaildirTestCase()
MaildirTestCase.setUp()
test_nonempty_maildir_both()
