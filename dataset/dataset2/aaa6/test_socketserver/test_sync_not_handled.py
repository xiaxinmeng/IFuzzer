import contextlib
import io
import os
import select
import signal
import socket
import tempfile
import threading
import unittest
import socketserver
import test.support
from test.support import reap_children, verbose
from test.support import os_helper
from test.support import socket_helper
from test.support import threading_helper
import test_socketserver

def test_sync_not_handled():
    with ErrorHandlerTest.assertRaises(SystemExit):
        test_socketserver.BaseErrorTestServer(SystemExit)
    ErrorHandlerTest.check_result(handled=False)

ErrorHandlerTest = test_socketserver.ErrorHandlerTest()
test_sync_not_handled()
