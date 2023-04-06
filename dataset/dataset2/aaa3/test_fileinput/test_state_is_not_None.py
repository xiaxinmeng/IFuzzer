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

def test_state_is_not_None():
    """Tests fileinput.isstdin() when fileinput._state is not None.
           Ensure that it invokes fileinput._state.isstdin() exactly once,
           returns whatever it returns, and does not modify fileinput._state
           to point to a different object."""
    isstdin_retval = object()
    instance = test_fileinput.MockFileInput()
    instance.return_values['isstdin'] = isstdin_retval
    fileinput._state = instance
    retval = fileinput.isstdin()
    Test_fileinput_close.assertExactlyOneInvocation(instance, 'isstdin')
    Test_fileinput_close.assertIs(retval, isstdin_retval)
    Test_fileinput_close.assertIs(fileinput._state, instance)

Test_fileinput_close = test_fileinput.Test_fileinput_close()
test_state_is_not_None()
