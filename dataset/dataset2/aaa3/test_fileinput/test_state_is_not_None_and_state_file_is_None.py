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

def test_state_is_not_None_and_state_file_is_None():
    """Tests invoking fileinput.input() when fileinput._state is not None
           but its _file attribute *is* None.  Expect it to create and return
           a new fileinput.FileInput object with all method parameters passed
           explicitly to the __init__() method; also ensure that
           fileinput._state is set to the returned instance."""
    instance = test_fileinput.MockFileInput()
    instance._file = None
    fileinput._state = instance
    Test_fileinput_input.do_test_call_input()

Test_fileinput_input = test_fileinput.Test_fileinput_input()
test_state_is_not_None_and_state_file_is_None()
