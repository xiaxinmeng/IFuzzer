import errno
import os
import select
import socket
import time
import unittest
from operator import lt, le, gt, ge
import test_kqueue

def test_create_queue():
    kq = select.kqueue()
    TestKQueue.assertTrue(kq.fileno() > 0, kq.fileno())
    TestKQueue.assertTrue(not kq.closed)
    kq.close()
    TestKQueue.assertTrue(kq.closed)
    TestKQueue.assertRaises(ValueError, kq.fileno)

TestKQueue = test_kqueue.TestKQueue()
test_create_queue()
