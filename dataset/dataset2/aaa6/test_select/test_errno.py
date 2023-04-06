import errno
import os
import select
import subprocess
import sys
import textwrap
import unittest
from test import support
import test_select

@unittest.skipIf(sys.platform.startswith('freebsd'), 'skip because of a FreeBSD bug: kern/155606')
def test_errno():
    with open(__file__, 'rb') as fp:
        fd = fp.fileno()
        fp.close()
        try:
            select.select([fd], [], [], 0)
        except OSError as err:
            SelectTestCase.assertEqual(err.errno, errno.EBADF)
        else:
            SelectTestCase.fail('exception not raised')

SelectTestCase = test_select.SelectTestCase()
test_errno()
