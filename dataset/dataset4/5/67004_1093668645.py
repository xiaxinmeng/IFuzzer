class TestStringMethods(unittest.TestCase):

    @unittest.expectedFailure
    def test_upper(self):
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()