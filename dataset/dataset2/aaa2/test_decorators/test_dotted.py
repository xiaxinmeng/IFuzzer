import unittest
import test_decorators

def test_dotted():
    decorators = test_decorators.MiscDecorators()

    @decorators.author('Cleese')
    def foo():
        return 42
    TestDecorators.assertEqual(foo(), 42)
    TestDecorators.assertEqual(foo.author, 'Cleese')

TestDecorators = test_decorators.TestDecorators()
test_dotted()
