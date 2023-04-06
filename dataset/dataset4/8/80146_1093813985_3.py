DESCRIPT_REQUIRES_TYPE_RE = r"descriptor '\w+' requires a 'set' object but received a 'int'"

class FooTest(unittest.TestCase):

    def test_assertRaisesRegex(self):
        self.assertRaisesRegex(TypeError, DESCRIPT_REQUIRES_TYPE_RE, set.add, 0)

    def test_assertRaisesRegex_contextman(self):
        with self.assertRaisesRegex(TypeError, DESCRIPT_REQUIRES_TYPE_RE):
            set.add(0)

if __name__ == "__main__":
    unittest.main()