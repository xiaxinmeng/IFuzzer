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

def test_strsignal():
    PosixTests.assertIn('Interrupt', signal.strsignal(signal.SIGINT))
    PosixTests.assertIn('Terminated', signal.strsignal(signal.SIGTERM))
    PosixTests.assertIn('Hangup', signal.strsignal(signal.SIGHUP))

PosixTests = test_signal.PosixTests()
test_strsignal()
