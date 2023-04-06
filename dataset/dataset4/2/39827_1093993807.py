import unittest
class TestStats(unittest.TestSuite):
    def testtwo(self):
        self.assertEqual(2,2)
suite = unittest.TestSuite([TestStats('testtwo')])
unittest.TextTestRunner(verbosity=2).run(suite)