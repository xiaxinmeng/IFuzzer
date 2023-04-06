import errno
import os
import random
import signal
import socket
import statistics
import subprocess
import sys
import time
import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok, spawn_python
import _testcapi
import test_signal

def test_setting_signal_handler_to_none_raises_error():
    PosixTests.assertRaises(TypeError, signal.signal, signal.SIGUSR1, None)

PosixTests = test_signal.PosixTests()
test_setting_signal_handler_to_none_raises_error()
