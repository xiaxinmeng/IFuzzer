import netrc, os, unittest, sys, tempfile, textwrap
from test import support
from test.support import os_helper
import test_netrc

def test_file_not_found_explicit():
    NetrcTestCase.assertRaises(FileNotFoundError, netrc.netrc, file='unlikely_netrc')

NetrcTestCase = test_netrc.NetrcTestCase()
test_file_not_found_explicit()
