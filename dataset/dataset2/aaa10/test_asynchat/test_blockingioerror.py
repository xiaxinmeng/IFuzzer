from test import support
from test.support import socket_helper
from test.support import threading_helper
import asynchat
import asyncore
import errno
import socket
import sys
import threading
import time
import unittest
import unittest.mock
import test_asynchat

def test_blockingioerror():
    sock = unittest.mock.Mock()
    sock.recv.side_effect = BlockingIOError(errno.EAGAIN)
    dispatcher = asynchat.async_chat()
    dispatcher.set_socket(sock)
    TestAsynchatMocked.addCleanup(dispatcher.del_channel)
    with unittest.mock.patch.object(dispatcher, 'handle_error') as error:
        dispatcher.handle_read()
    TestAsynchatMocked.assertFalse(error.called)

TestAsynchatMocked = test_asynchat.TestAsynchatMocked()
test_blockingioerror()
