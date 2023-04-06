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

def test_permissions_after_flush():
    mode = os.stat(_TestSingleFile._path).st_mode | 438
    os.chmod(_TestSingleFile._path, mode)
    _TestSingleFile._box.add(_TestSingleFile._template % 0)
    i = _TestSingleFile._box.add(_TestSingleFile._template % 1)
    _TestSingleFile._box.remove(i)
    _TestSingleFile._box.flush()
    _TestSingleFile.assertEqual(os.stat(_TestSingleFile._path).st_mode, mode)

_TestSingleFile = test_mailbox._TestSingleFile()
_TestSingleFile.setUp()
test_permissions_after_flush()
