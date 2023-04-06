
import unittest

def foo():
    for x in [1, 2, 'oops', 4]:
        print(x + 100)

class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertIs(foo(), None)

if __name__ == '__main__':
    unittest.main()
