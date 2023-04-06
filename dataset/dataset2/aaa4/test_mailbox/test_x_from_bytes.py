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

def test_x_from_bytes():
    for class_ in TestMessageConversion.all_mailbox_types:
        msg = class_(test_mailbox._bytes_sample_message)
        TestMessageConversion._check_sample(msg)

TestMessageConversion = test_mailbox.TestMessageConversion()
test_x_from_bytes()
