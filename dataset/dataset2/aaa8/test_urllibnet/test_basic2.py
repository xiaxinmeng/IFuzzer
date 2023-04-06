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

def test_basic(urlopenNetworkTests):
# Simple test expected to pass.
    with urlopenNetworkTests.urlopen(urlopenNetworkTests.url) as open_url:
        for attr in ("read", "readline", "readlines", "fileno", "close",
             "info", "geturl"):
	        urlopenNetworkTests.assertTrue(hasattr(open_url, attr), "object returned from "
	                "urlopen lacks the %s attribute" % attr)
        urlopenNetworkTests.assertTrue(open_url.read(), "calling 'read' failed")

urlopenNetworkTests = test_urllibnet.urlopenNetworkTests()

test_basic(urlopenNetworkTests)
