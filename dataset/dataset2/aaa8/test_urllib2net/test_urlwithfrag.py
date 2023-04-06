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

def test_urlwithfrag():
    urlwith_frag = 'http://www.pythontest.net/index.html#frag'
    with socket_helper.transient_internet(urlwith_frag):
        req = urllib.request.Request(urlwith_frag)
        res = urllib.request.urlopen(req)
        OtherNetworkTests.assertEqual(res.geturl(), 'http://www.pythontest.net/index.html#frag')

OtherNetworkTests = test_urllib2net.OtherNetworkTests()
test_urlwithfrag()
