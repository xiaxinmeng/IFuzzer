import sys
import os
import tempfile
import textwrap
import unittest

import test_pkg

@unittest.skipIf(sys.flags.optimize >= 2, 'Docstrings are omitted with -O2 and above')
def test_8():
    hier = [('t8', None), ('t8 __init__' + os.extsep + 'py', "'doc for t8'")]
    TestPkg.mkhier(hier)
    import t8
    TestPkg.assertEqual(t8.__doc__, 'doc for t8')

TestPkg = test_pkg.TestPkg()
TestPkg.setUp()
test_8()
