import unittest

def this_fails():
    a = 1 + None

class TestExample(unittest.TestCase):

    def test_this(self):
        try:
            this_fails()
        except Exception:
            self.fail('Fail')

if __name__ == '__main__':
    unittest.run()