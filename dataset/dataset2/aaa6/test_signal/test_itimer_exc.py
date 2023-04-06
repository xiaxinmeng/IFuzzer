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

def test_itimer_exc():
    ItimerTest.assertRaises(signal.ItimerError, signal.setitimer, -1, 0)
    if 0:
        ItimerTest.assertRaises(signal.ItimerError, signal.setitimer, signal.ITIMER_REAL, -1)

ItimerTest = test_signal.ItimerTest()
test_itimer_exc()
