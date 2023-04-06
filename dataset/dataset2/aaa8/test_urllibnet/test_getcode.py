import unittest
from test import support
from test.support import os_helper
from test.support import socket_helper
import contextlib
import socket
import urllib.parse
import urllib.request
import os
import email.message
import time
import test_urllibnet

def test_getcode():
    URL = urlopenNetworkTests.url + 'XXXinvalidXXX'
    with socket_helper.transient_internet(URL):
        with urlopenNetworkTests.assertWarns(DeprecationWarning):
            open_url = urllib.request.FancyURLopener().open(URL)
        try:
            code = open_url.getcode()
        finally:
            open_url.close()
        urlopenNetworkTests.assertEqual(code, 404)

urlopenNetworkTests = test_urllibnet.urlopenNetworkTests()
test_getcode()
