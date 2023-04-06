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

def test_bad_address():
    bogus_domain = 'sadflkjsasf.i.nvali.d.'
    try:
        socket.gethostbyname(bogus_domain)
    except OSError:
        pass
    else:
        urlopenNetworkTests.skipTest('%r should not resolve for test to work' % bogus_domain)
    failure_explanation = 'opening an invalid URL did not raise OSError; can be caused by a broken DNS server (e.g. returns 404 or hijacks page)'
    with urlopenNetworkTests.assertRaises(OSError, msg=failure_explanation):
        urllib.request.urlopen('http://{}/'.format(bogus_domain))

urlopenNetworkTests = test_urllibnet.urlopenNetworkTests()
test_bad_address()
