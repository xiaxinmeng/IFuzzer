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

def test_readlines():
    with urlopenNetworkTests.urlopen(urlopenNetworkTests.url) as open_url:
        urlopenNetworkTests.assertIsInstance(open_url.readline(), bytes, 'readline did not return a string')
        urlopenNetworkTests.assertIsInstance(open_url.readlines(), list, 'readlines did not return a list')

urlopenNetworkTests = test_urllibnet.urlopenNetworkTests()
test_readlines()
