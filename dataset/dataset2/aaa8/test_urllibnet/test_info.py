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

def test_info():
    with urlopenNetworkTests.urlopen(urlopenNetworkTests.url) as open_url:
        info_obj = open_url.info()
        urlopenNetworkTests.assertIsInstance(info_obj, email.message.Message, "object returned by 'info' is not an instance of email.message.Message")
        urlopenNetworkTests.assertEqual(info_obj.get_content_subtype(), 'html')

urlopenNetworkTests = test_urllibnet.urlopenNetworkTests()
test_info()
