import errno
import os
import select
import socket
import time
import unittest
import test_epoll

def test_fd_non_inheritable():
    epoll = select.epoll()
    TestEPoll.addCleanup(epoll.close)
    TestEPoll.assertEqual(os.get_inheritable(epoll.fileno()), False)

TestEPoll = test_epoll.TestEPoll()
test_fd_non_inheritable()
