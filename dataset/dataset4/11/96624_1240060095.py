import sys
from unittest.mock import patch

if 0: # change to 1 to see "tu.dummy" fail.

    # Inline test_dotted_but_module_not_loaded
    # This exercises the AttributeError branch of _dot_lookup.

    # make sure it's there
    import test.test_unittest.testmock.support
    # now make sure it's not:
    with patch.dict('sys.modules'):
        del sys.modules['test.test_unittest.testmock.support']
        del sys.modules['test.test_unittest.testmock']
        del sys.modules['test.test_unittest']
        del sys.modules['unittest']

        # now make sure we can patch based on a dotted path:
        @patch('test.test_unittest.testmock.support.X')
        def test(mock):
            print(mock)
        test()


# The part that fails in test_loadTestsFromName__module_not_loaded
module_name = 'test.test_unittest.dummy'
sys.modules.pop(module_name, None)
tu = __import__(module_name).test_unittest
tu.dummy