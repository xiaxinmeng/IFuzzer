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

def test_relock():
    msg = 'Subject: sub\n\nbody\n'
    key1 = _TestMboxMMDF._box.add(msg)
    _TestMboxMMDF._box.flush()
    _TestMboxMMDF._box.close()
    _TestMboxMMDF._box = _TestMboxMMDF._factory(_TestMboxMMDF._path)
    _TestMboxMMDF._box.lock()
    key2 = _TestMboxMMDF._box.add(msg)
    _TestMboxMMDF._box.flush()
    _TestMboxMMDF.assertTrue(_TestMboxMMDF._box._locked)
    _TestMboxMMDF._box.close()

_TestMboxMMDF = test_mailbox._TestMboxMMDF()
_TestMboxMMDF.setUp()
test_relock()
