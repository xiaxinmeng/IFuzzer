import netrc, os, unittest, sys, tempfile, textwrap
from test import support
from test.support import os_helper
import test_netrc

def test_comment_at_end_of_machine_line_pass_has_hash():
    NetrcTestCase._test_comment('            machine foo.domain.com login bar password #pass #comment\n            machine bar.domain.com login foo password pass\n            ', '#pass')

NetrcTestCase = test_netrc.NetrcTestCase()
test_comment_at_end_of_machine_line_pass_has_hash()