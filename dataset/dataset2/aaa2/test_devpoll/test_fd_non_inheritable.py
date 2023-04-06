import os
import random
import select
import unittest
from test.support import run_unittest, cpython_only
from _testcapi import USHRT_MAX
import test_devpoll

def test_fd_non_inheritable():
    devpoll = select.devpoll()
    DevPollTests.addCleanup(devpoll.close)
    DevPollTests.assertEqual(os.get_inheritable(devpoll.fileno()), False)

DevPollTests = test_devpoll.DevPollTests()
test_fd_non_inheritable()
