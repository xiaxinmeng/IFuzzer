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
def test_ftp_timeout():
    with socket_helper.transient_internet(TimeoutTest.FTP_HOST):
        u =test_urllib2net._urlopen_with_retry(TimeoutTest.FTP_HOST, timeout=60)
        TimeoutTest.addCleanup(u.close)
        TimeoutTest.assertEqual(u.fp.fp.raw._sock.gettimeout(), 60)

TimeoutTest = test_urllib2net.TimeoutTest()
test_ftp_timeout()
