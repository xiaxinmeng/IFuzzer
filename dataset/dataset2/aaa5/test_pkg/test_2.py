import sys
import os
import tempfile
import textwrap
import unittest

import test_pkg

def test_2():
    hier = [('t2', None), ('t2 __init__.py', "'doc for t2'"), ('t2 sub', None), ('t2 sub __init__.py', ''), ('t2 sub subsub', None), ('t2 sub subsub __init__.py', 'spam = 1')]
    TestPkg.mkhier(hier)
    import t2.sub
    import t2.sub.subsub
    TestPkg.assertEqual(t2.__name__, 't2')
    TestPkg.assertEqual(t2.sub.__name__, 't2.sub')
    TestPkg.assertEqual(t2.sub.subsub.__name__, 't2.sub.subsub')
    s = "\n            import t2\n            from t2 import *\n            TestPkg.assertEqual(dir(), ['TestPkg', 'sub', 't2'])\n            "
    TestPkg.run_code(s)
    from t2 import sub
    from t2.sub import subsub
    from t2.sub.subsub import spam
    TestPkg.assertEqual(sub.__name__, 't2.sub')
    TestPkg.assertEqual(subsub.__name__, 't2.sub.subsub')
    TestPkg.assertEqual(sub.subsub.__name__, 't2.sub.subsub')
    for name in ['spam', 'sub', 'subsub', 't2']:
        TestPkg.assertTrue(locals()['name'], 'Failed to import %s' % name)
    import t2.sub
    import t2.sub.subsub
    TestPkg.assertEqual(t2.__name__, 't2')
    TestPkg.assertEqual(t2.sub.__name__, 't2.sub')
    TestPkg.assertEqual(t2.sub.subsub.__name__, 't2.sub.subsub')
    s = "\n            from t2 import *\n            TestPkg.assertEqual(dir(), ['TestPkg', 'sub'])\n            "
    TestPkg.run_code(s)

TestPkg = test_pkg.TestPkg()
TestPkg.setUp()
test_2()
