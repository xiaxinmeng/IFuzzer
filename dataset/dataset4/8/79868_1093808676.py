import unittest

class StdErrUnitTests(unittest.TestCase):

    def test_function_name(self):
        expected = "testing.main_unit_tests.test_dictionaryBasicLogging:416 - dictionary\n" \
                "testing.main_unit_tests.test_dictionaryBasicLogging:417 - dictionary {1: 'defined_chunk'}"

        actual = "15:49:35:912.348986 - testing.main_unit_tests - dictionary\n" \
                "15:49:35:918.879986 - testing.main_unit_tests - dictionary {1: 'defined_chunk'}"

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()