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

def test_custom_headers():
    url = support.TEST_HTTP_URL
    with socket_helper.transient_internet(url):
        opener = urllib.request.build_opener()
        request = urllib.request.Request(url)
        OtherNetworkTests.assertFalse(request.header_items())
        opener.open(request)
        OtherNetworkTests.assertTrue(request.header_items())
        OtherNetworkTests.assertTrue(request.has_header('User-agent'))
        request.add_header('User-Agent', 'Test-Agent')
        opener.open(request)
        OtherNetworkTests.assertEqual(request.get_header('User-agent'), 'Test-Agent')

OtherNetworkTests = test_urllib2net.OtherNetworkTests()
test_custom_headers()
