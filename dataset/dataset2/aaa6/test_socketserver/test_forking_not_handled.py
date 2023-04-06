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

@test_socketserver.requires_forking
def test_forking_not_handled():
    test_socketserver.ForkingErrorTestServer(SystemExit)
    ErrorHandlerTest.check_result(handled=False)

ErrorHandlerTest = test_socketserver.ErrorHandlerTest()
test_forking_not_handled()
