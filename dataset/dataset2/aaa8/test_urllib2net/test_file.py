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

def test_file():
    TESTFN = os_helper.TESTFN
    f = open(TESTFN, 'w')
    try:
        f.write('hi there\n')
        f.close()
        urls = ['file:' + sanepathname2url(os.path.abspath(TESTFN)), ('file:///nonsensename/etc/passwd', None, urllib.error.URLError)]
        OtherNetworkTests._test_urls(urls, OtherNetworkTests._extra_handlers(), retry=True)
    finally:
        os.remove(TESTFN)
    OtherNetworkTests.assertRaises(ValueError, urllib.request.urlopen, './relative_path/to/file')

OtherNetworkTests = test_urllib2net.OtherNetworkTests()
test_file()
