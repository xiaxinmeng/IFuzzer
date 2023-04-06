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

def test_x_to_plain():
    for class_ in TestMessageConversion.all_mailbox_types:
        msg = class_(test_mailbox._sample_message)
        msg_plain = mailbox.Message(msg)
        TestMessageConversion._check_sample(msg_plain)

TestMessageConversion = test_mailbox.TestMessageConversion()
test_x_to_plain()
