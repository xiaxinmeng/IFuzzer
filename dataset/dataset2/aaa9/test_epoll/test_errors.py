import errno
import os
import select
import socket
import time
import unittest
import test_epoll

def test_errors():
    TestEPoll.assertRaises(ValueError, select.epoll, -2)
    TestEPoll.assertRaises(ValueError, select.epoll().register, -1, select.EPOLLIN)

TestEPoll = test_epoll.TestEPoll()
test_errors()
