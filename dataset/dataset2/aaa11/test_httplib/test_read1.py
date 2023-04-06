import errno
from http import client, HTTPStatus
import io
import itertools
import os
import array
import re
import socket
import threading
import warnings
import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.support import warnings_helper
from test.ssl_servers import make_https_server
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import ssl
import test_httplib

def test_read1():
    resp = ExtendedReadTest.resp

    def r():
        res = resp.read1(4)
        ExtendedReadTest.assertLessEqual(len(res), 4)
        return res
    readliner = test_httplib.Readliner(r)
    ExtendedReadTest._verify_readline(readliner.readline, ExtendedReadTest.lines_expected)

ExtendedReadTest = test_httplib.ExtendedReadTest()
ExtendedReadTest.setUp()
test_read1()
