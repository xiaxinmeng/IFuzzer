import errno
import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
from test.test_urllib2 import sanepathname2url
import os
import socket
import urllib.error
import urllib.request
import sys
import logging
import time
import logging
import test_urllib2net

@test_urllib2net.skip_ftp_test_on_travis
def test_ftp_basic():
    TimeoutTest.assertIsNone(socket.getdefaulttimeout())
    with socket_helper.transient_internet(TimeoutTest.FTP_HOST, timeout=None):
        u = test_urllib2net._urlopen_with_retry(TimeoutTest.FTP_HOST)
        TimeoutTest.addCleanup(u.close)
        TimeoutTest.assertIsNone(u.fp.fp.raw._sock.gettimeout())

TimeoutTest = test_urllib2net.TimeoutTest()
test_ftp_basic()
