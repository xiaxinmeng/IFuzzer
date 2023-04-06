import mailcap
import os
import copy
import test.support
from test.support import os_helper
import unittest
import sys
import test_mailcap

@unittest.skipUnless(os.name == 'posix', "Requires 'test' command on system")
@unittest.skipIf(sys.platform == 'vxworks', "'test' command is not supported on VxWorks")
def test_test():
    caps = {'test/pass': [{'test': 'test 1 -eq 1'}], 'test/fail': [{'test': 'test 1 -eq 0'}]}
    cases = [([caps, 'test/pass', 'test'], {}, ('test 1 -eq 1', {'test': 'test 1 -eq 1'})), ([caps, 'test/fail', 'test'], {}, (None, None))]
    FindmatchTest._run_cases(cases)

FindmatchTest = test_mailcap.FindmatchTest()
test_test()
