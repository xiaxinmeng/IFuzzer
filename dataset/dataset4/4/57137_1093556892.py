import unittest
class MyTest(unittest.TestCase):
    def test_a(self):
        b = 1
        exec(compile("a = b + 1", '', 'single'))
        assert a == 2
if __name__ == '__main__':
    unittest.main()