import netrc, os, unittest, sys, tempfile, textwrap
from test import support
from test.support import os_helper
import test_netrc

def test_file_not_found_in_home():
    with os_helper.temp_cwd(None) as d:
        with os_helper.EnvironmentVarGuard() as environ:
            environ.set('HOME', d)
            NetrcTestCase.assertRaises(FileNotFoundError, netrc.netrc)

NetrcTestCase = test_netrc.NetrcTestCase()
test_file_not_found_in_home()
