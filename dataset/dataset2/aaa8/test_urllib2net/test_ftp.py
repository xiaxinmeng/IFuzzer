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
def test_ftp():
    urls = ['ftp://www.pythontest.net/README', ('ftp://www.pythontest.net/non-existent-file', None, urllib.error.URLError)]
    OtherNetworkTests._test_urls(urls, OtherNetworkTests._extra_handlers())

OtherNetworkTests = test_urllib2net.OtherNetworkTests()
test_ftp()
