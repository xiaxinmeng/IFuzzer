import test.support
from test.support import threading_helper
from test.support import verbose, cpython_only
from test.support.import_helper import import_module
from test.support.script_helper import assert_python_ok, assert_python_failure
import random
import sys
import _thread
import threading
import time
import unittest
import weakref
import os
import subprocess
import signal
import textwrap
from unittest import mock
from test import lock_tests
from test import support
import _testcapi
import test_threading

def test_atexit_called_once():
    (rc, out, err) = assert_python_ok('-c', 'if True:\n            import threading\n            from unittest.mock import Mock\n\n            mock = Mock()\n            threading._register_atexit(mock)\n            mock.assert_not_called()\n            # force early shutdown to ensure it was called once\n            threading._shutdown()\n            mock.assert_called_once()\n        ')
    AtexitTests.assertFalse(err)

AtexitTests = test_threading.AtexitTests()
test_atexit_called_once()
