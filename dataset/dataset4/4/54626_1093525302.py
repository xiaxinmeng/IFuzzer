class UnicodeTest(unittest.TestCase):
    def test_unicode_docstring(self):
        u"""docstring with unicode character. t\xe4st"""
        self.assertEqual(1+1, 2)

if __name__ == '__main__':
    unittest.main()