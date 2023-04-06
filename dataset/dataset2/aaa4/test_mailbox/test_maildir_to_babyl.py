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

def test_maildir_to_babyl():
    msg_maildir = mailbox.MaildirMessage(test_mailbox._sample_message)
    pairs = (('D', ['unseen']), ('F', ['unseen']), ('P', ['unseen', 'forwarded']), ('R', ['unseen', 'answered']), ('S', []), ('T', ['unseen', 'deleted']), ('DFPRST', ['deleted', 'answered', 'forwarded']))
    for (setting, result) in pairs:
        msg_maildir.set_flags(setting)
        TestMessageConversion.assertEqual(mailbox.BabylMessage(msg_maildir).get_labels(), result)

TestMessageConversion = test_mailbox.TestMessageConversion()
test_maildir_to_babyl()
