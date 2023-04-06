class TestFoo(unittest.TestCase):

    def test_foo(self):
        self.assertEquals(1, 1)


if __name__ == "__main__":
    unittest.main()