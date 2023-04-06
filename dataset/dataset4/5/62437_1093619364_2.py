import unittest
class MyTest(unittest.TestCase):
    def test_example(self):
        # this fails
        self.assertRaisesRegexp(ValueError, 'invalid literal for.*XYZ$',
                        int, 'XYZ')
    def test_option1(self):
        self.assertRaisesRegexp(ValueError, 'invalid literal for.*XYZ',
                                int, 'XYZ')
    def test_option2(self):
        self.assertRaisesRegexp(ValueError, 'invalid literal for.*XYZ\'$',
                                int, 'XYZ')

unittest.main()