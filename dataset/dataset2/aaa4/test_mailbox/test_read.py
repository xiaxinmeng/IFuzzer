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

def test_read():
    TestProxyFile._file.write(bytes('***bar***', 'ascii'))
    TestProxyFile._test_read(mailbox._PartialFile(TestProxyFile._file, 3, 6))

TestProxyFile = test_mailbox.TestProxyFile()
TestProxyFile.setUp()
test_read()
