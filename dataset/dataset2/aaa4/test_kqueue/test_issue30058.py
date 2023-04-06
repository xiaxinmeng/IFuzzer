import errno
import os
import select
import socket
import time
import unittest
from operator import lt, le, gt, ge
import test_kqueue

def test_issue30058():
    kq = select.kqueue()
    (a, b) = socket.socketpair()
    ev = select.kevent(a, select.KQ_FILTER_READ, select.KQ_EV_ADD | select.KQ_EV_ENABLE)
    kq.control([ev], 0)
    kq.control((ev,), 0)

    class BadList:

        def __len__(TestKQueue):
            return 0

        def __iter__(TestKQueue):
            for i in range(100):
                yield ev
    kq.control(BadList(), 0)
    kq.control(iter([ev]), 0)
    a.close()
    b.close()
    kq.close()

TestKQueue = test_kqueue.TestKQueue()
test_issue30058()
