
import unittest
import sys

class MyTest(unittest.TestCase):

    def __init__(self, testName, extraArg):
        super(MyTest, self).__init__(testName)
        self.myExtraArg = extraArg

    def test_something(self):
        print(self.myExtraArg)

extraArg = sys.argv.pop()
suite = unittest.TestSuite()
suite.addTest(MyTest('test_something', extraArg))
unittest.TextTestRunner(verbosity=2).run(suite)
