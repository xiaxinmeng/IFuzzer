import unittest
import glob
import os.path
import test.support
from test.support.script_helper import assert_python_failure
import test_crashers

@unittest.skip('these tests are too fragile')
@test.support.cpython_only
def test_crashers_crash():
    for fname in glob.glob(CRASHER_FILES):
        if os.path.basename(fname) in infinite_loops:
            continue
        if test.support.verbose:
            print('Checking crasher:', fname)
        assert_python_failure(fname)

CrasherTest = test_crashers.CrasherTest()
test_crashers_crash()
