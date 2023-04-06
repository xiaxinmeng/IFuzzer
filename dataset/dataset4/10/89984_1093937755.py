import unittest

class uTest(unittest.TestCase):
	pass

uTest = uTest()

with uTest.assertRaisesRegex(Exception, 'aaa'):
     aab