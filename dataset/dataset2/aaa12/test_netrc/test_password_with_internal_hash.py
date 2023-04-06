import netrc, os, unittest, sys, tempfile, textwrap
from test import support
from test.support import os_helper
import test_netrc

def test_password_with_internal_hash():
    NetrcTestCase._test_passwords('            machine host.domain.com login log password pa#ss account acct\n            ', 'pa#ss')

NetrcTestCase = test_netrc.NetrcTestCase()
test_password_with_internal_hash()
