class T(unittest.TestCase):
    def test_items_equal(self):
        # this test fails, but should succeed
        a = [{2,4}, {1,2}]
        b = a[::-1]
        self.assertItemsEqual(a, b)