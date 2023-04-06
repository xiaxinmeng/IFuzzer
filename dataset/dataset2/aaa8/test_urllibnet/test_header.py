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

def test_header():
    with urlretrieveNetworkTests.urlretrieve(urlretrieveNetworkTests.logo) as (file_location, info):
        urlretrieveNetworkTests.assertIsInstance(info, email.message.Message, 'info is not an instance of email.message.Message')

urlretrieveNetworkTests = test_urllibnet.urlretrieveNetworkTests()
test_header()
