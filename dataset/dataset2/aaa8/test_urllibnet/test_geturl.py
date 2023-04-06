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

def test_geturl():
    with urlopenNetworkTests.urlopen(urlopenNetworkTests.url) as open_url:
        gotten_url = open_url.geturl()
        urlopenNetworkTests.assertEqual(gotten_url, urlopenNetworkTests.url)

urlopenNetworkTests = test_urllibnet.urlopenNetworkTests()
test_geturl()
