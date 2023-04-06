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

def test_specified_path():
    with urlretrieveNetworkTests.urlretrieve(urlretrieveNetworkTests.logo, os_helper.TESTFN) as (file_location, info):
        urlretrieveNetworkTests.assertEqual(file_location, os_helper.TESTFN)
        urlretrieveNetworkTests.assertTrue(os.path.exists(file_location))
        with open(file_location, 'rb') as f:
            urlretrieveNetworkTests.assertTrue(f.read(), 'reading from temporary file failed')

urlretrieveNetworkTests = test_urllibnet.urlretrieveNetworkTests()
test_specified_path()
