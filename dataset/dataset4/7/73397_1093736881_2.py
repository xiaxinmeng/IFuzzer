import unittest

class TestGen(unittest.TestCase):
    def test_gen(self):
        spam = Spam()
        self.assertEqual(spam.get_next(), 1)
        with self.assertRaises(ZeroDivisionError):
            spam.get_next()
        self.assertEqual(spam.get_next(), 3)

unittest.main()