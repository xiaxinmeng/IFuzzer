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

def test_redirect_url_withfrag():
    redirect_url_with_frag = 'http://www.pythontest.net/redir/with_frag/'
    with socket_helper.transient_internet(redirect_url_with_frag):
        req = urllib.request.Request(redirect_url_with_frag)
        res = urllib.request.urlopen(req)
        OtherNetworkTests.assertEqual(res.geturl(), 'http://www.pythontest.net/elsewhere/#frag')

OtherNetworkTests = test_urllib2net.OtherNetworkTests()
test_redirect_url_withfrag()
