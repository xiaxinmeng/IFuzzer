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

def test_basic():
    with urlretrieveNetworkTests.urlretrieve(urlretrieveNetworkTests.logo) as (file_location, info):
        urlretrieveNetworkTests.assertTrue(os.path.exists(file_location), 'file location returned by urlretrieve is not a valid path')
        with open(file_location, 'rb') as f:
            urlretrieveNetworkTests.assertTrue(f.read(), 'reading from the file location returned by urlretrieve failed')

urlretrieveNetworkTests = test_urllibnet.urlretrieveNetworkTests()

test_basic()
