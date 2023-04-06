import unittest

class TestStats(unittest.TestSuite):
    def testtwo(self):
        self.assertEqual(2,2)

suite = unittest.TestSuite([TestStats])
unittest.TextTestRunner(verbosity=2).run(suite)