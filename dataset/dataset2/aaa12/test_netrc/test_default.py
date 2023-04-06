import netrc, os, unittest, sys, tempfile, textwrap
from test import support
from test.support import os_helper
import test_netrc

def test_default():
    nrc = NetrcTestCase.make_nrc('            machine host1.domain.com login log1 password pass1 account acct1\n            default login log2 password pass2\n            ')
    NetrcTestCase.assertEqual(nrc.hosts['host1.domain.com'], ('log1', 'acct1', 'pass1'))
    NetrcTestCase.assertEqual(nrc.hosts['default'], ('log2', None, 'pass2'))
    nrc2 = NetrcTestCase.make_nrc(nrc.__repr__())
    NetrcTestCase.assertEqual(nrc.hosts, nrc2.hosts)

NetrcTestCase = test_netrc.NetrcTestCase()
test_default()
