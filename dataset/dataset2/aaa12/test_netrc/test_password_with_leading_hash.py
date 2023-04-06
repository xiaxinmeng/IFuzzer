import netrc, os, unittest, sys, tempfile, textwrap
from test import support
from test.support import os_helper
import test_netrc

def test_password_with_leading_hash():
    NetrcTestCase._test_passwords('            machine host.domain.com login log password #pass account acct\n            ', '#pass')

NetrcTestCase = test_netrc.NetrcTestCase()
test_password_with_leading_hash()
