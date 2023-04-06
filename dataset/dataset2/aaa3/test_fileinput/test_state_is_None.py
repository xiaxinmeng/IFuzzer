import os
import sys
import re
import fileinput
import collections
import builtins
import tempfile
import unittest

import gzip
from io import BytesIO, StringIO
from fileinput import FileInput, hook_encoded
from pathlib import Path
from test.support import verbose
from test.support.os_helper import TESTFN
from test.support.os_helper import unlink as safe_unlink
from test.support import os_helper
from test.support import warnings_helper
from test import support
from unittest import mock
import test_fileinput

def test_state_is_None():
    """Tests fileinput.isstdin() when fileinput._state is None.
           Ensure that it raises RuntimeError with a meaningful error message
           and does not modify fileinput._state"""
    fileinput._state = None
    with Test_fileinput_input.assertRaises(RuntimeError) as cm:
        fileinput.isstdin()
    Test_fileinput_input.assertEqual(('no active input()',), cm.exception.args)
    Test_fileinput_input.assertIsNone(fileinput._state)

Test_fileinput_input = test_fileinput.Test_fileinput_input()
test_state_is_None()
