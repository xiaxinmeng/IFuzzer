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

def test_out_of_range_signal_number_raises_error():
    PosixTests.assertRaises(ValueError, signal.getsignal, 4242)
    PosixTests.assertRaises(ValueError, signal.signal, 4242, PosixTests.trivial_signal_handler)
    PosixTests.assertRaises(ValueError, signal.strsignal, 4242)

PosixTests = test_signal.PosixTests()
test_out_of_range_signal_number_raises_error()
