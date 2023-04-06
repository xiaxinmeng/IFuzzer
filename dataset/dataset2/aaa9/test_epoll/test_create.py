import errno
import os
import select
import socket
import time
import unittest
import test_epoll

def test_create():
    try:
        ep = select.epoll(16)
    except OSError as e:
        raise AssertionError(str(e))
    TestEPoll.assertTrue(ep.fileno() > 0, ep.fileno())
    TestEPoll.assertTrue(not ep.closed)
    ep.close()
    TestEPoll.assertTrue(ep.closed)
    TestEPoll.assertRaises(ValueError, ep.fileno)
    if hasattr(select, 'EPOLL_CLOEXEC'):
        select.epoll(-1, select.EPOLL_CLOEXEC).close()
        select.epoll(flags=select.EPOLL_CLOEXEC).close()
        select.epoll(flags=0).close()

TestEPoll = test_epoll.TestEPoll()
test_create()
