import errno
import os
import select
import socket
import time
import unittest
import test_epoll

def test_context_manager():
    with select.epoll(16) as ep:
        TestEPoll.assertGreater(ep.fileno(), 0)
        TestEPoll.assertFalse(ep.closed)
    TestEPoll.assertTrue(ep.closed)
    TestEPoll.assertRaises(ValueError, ep.fileno)

TestEPoll = test_epoll.TestEPoll()
test_context_manager()
