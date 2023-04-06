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

def test_mh_to_mh():
    msg = mailbox.MHMessage(test_mailbox._sample_message)
    msg.add_sequence('unseen')
    msg.add_sequence('replied')
    msg.add_sequence('flagged')
    TestMessageConversion.assertEqual(mailbox.MHMessage(msg).get_sequences(), ['unseen', 'replied', 'flagged'])

TestMessageConversion = test_mailbox.TestMessageConversion()
test_mh_to_mh()
