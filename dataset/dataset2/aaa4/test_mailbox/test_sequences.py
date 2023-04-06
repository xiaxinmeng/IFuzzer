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

def test_sequences():
    msg = mailbox.MHMessage(test_mailbox._sample_message)
    TestMH.assertEqual(msg.get_sequences(), [])
    msg.set_sequences(['foobar'])
    TestMH.assertEqual(msg.get_sequences(), ['foobar'])
    msg.set_sequences([])
    TestMH.assertEqual(msg.get_sequences(), [])
    msg.add_sequence('unseen')
    TestMH.assertEqual(msg.get_sequences(), ['unseen'])
    msg.add_sequence('flagged')
    TestMH.assertEqual(msg.get_sequences(), ['unseen', 'flagged'])
    msg.add_sequence('flagged')
    TestMH.assertEqual(msg.get_sequences(), ['unseen', 'flagged'])
    msg.remove_sequence('unseen')
    TestMH.assertEqual(msg.get_sequences(), ['flagged'])
    msg.add_sequence('foobar')
    TestMH.assertEqual(msg.get_sequences(), ['flagged', 'foobar'])
    msg.remove_sequence('replied')
    TestMH.assertEqual(msg.get_sequences(), ['flagged', 'foobar'])
    msg.set_sequences(['foobar', 'replied'])
    TestMH.assertEqual(msg.get_sequences(), ['foobar', 'replied'])

TestMH = test_mailbox.TestMH()
test_sequences()
