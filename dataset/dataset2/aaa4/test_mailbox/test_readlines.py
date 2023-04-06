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

def test_readlines():
    TestProxyFile._file.write(bytes('foo%sbar%sfred%sbob?????' % (os.linesep, os.linesep, os.linesep), 'ascii'))
    TestProxyFile._test_readlines(mailbox._PartialFile(TestProxyFile._file, 0, 13 + 3 * len(os.linesep)))

TestProxyFile = test_mailbox.TestProxyFile()
TestProxyFile.setUp()
test_readlines()
