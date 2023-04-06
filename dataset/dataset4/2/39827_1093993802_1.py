import unittest

class TestStats(unittest.TestSuite):

    def testtwo(self):
        self.assertEqual(2,2)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestStats))
unittest.TextTestRunner(verbosity=2).run(suite)