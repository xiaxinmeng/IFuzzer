import unittest
class MyTest(unittest.TestCase):
    def test_a(self):
        exec(compile("a = 1", '', 'single'))
        assert a == 1
if __name__ == '__main__':
    unittest.main()