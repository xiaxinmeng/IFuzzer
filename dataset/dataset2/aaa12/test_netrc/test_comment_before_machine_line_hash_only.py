import netrc, os, unittest, sys, tempfile, textwrap
from test import support
from test.support import os_helper
import test_netrc

def test_comment_before_machine_line_hash_only():
    NetrcTestCase._test_comment('            #\n            machine foo.domain.com login bar password pass\n            machine bar.domain.com login foo password pass\n            ')

NetrcTestCase = test_netrc.NetrcTestCase()
test_comment_before_machine_line_hash_only()
