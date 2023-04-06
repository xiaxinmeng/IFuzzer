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

def test_plain_to_x():
    for class_ in TestMessageConversion.all_mailbox_types:
        msg_plain = mailbox.Message(test_mailbox._sample_message)
        msg = class_(msg_plain)
        TestMessageConversion._check_sample(msg)

TestMessageConversion = test_mailbox.TestMessageConversion()
test_plain_to_x()
