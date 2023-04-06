import errno
import os
import select
import socket
import time
import unittest
from operator import lt, le, gt, ge
import test_kqueue

def test_fd_non_inheritable():
    kqueue = select.kqueue()
    TestKQueue.addCleanup(kqueue.close)
    TestKQueue.assertEqual(os.get_inheritable(kqueue.fileno()), False)

TestKQueue = test_kqueue.TestKQueue()
test_fd_non_inheritable()
