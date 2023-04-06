import os
import signal
import unittest
from test import support
from test.support import script_helper
import test_eintr

@unittest.skipUnless(hasattr(signal, 'setitimer'), 'requires setitimer()')
def test_all():
    script = support.findfile('_test_eintr.py')
    script_helper.run_test_script(script)

EINTRTests = test_eintr.EINTRTests()
test_all()
