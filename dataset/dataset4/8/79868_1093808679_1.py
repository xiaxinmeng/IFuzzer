import unittest

class StdErrUnitTests(unittest.TestCase):

    def test_function_name(self):
        expected = "a\nb"
        actual = "c\nd"

        self.assertEqual(expected, actual)

    def test_function_name_newlines_end(self):
        expected = "a\nb\n"
        actual = "c\nd\n"

        self.assertEqual(expected, actual) # produces extra new line at the diff in the end with \d\n


if __name__ == '__main__':
    unittest.main()