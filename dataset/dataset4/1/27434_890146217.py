import unittest

class TestDictDiffSlow(unittest.TestCase):

    def test_slow_assert_equal_dict(self):
        d1 = { i : i * 2 for i in range(10000) }
        d2= { i : i for i in range(10000) }
        self.assertDictEqual(d1, d2)


if __name__ == '__main__':
    unittest.main()