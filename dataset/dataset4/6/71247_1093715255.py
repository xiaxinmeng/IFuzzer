import unittest as u
class Test(u.TestCase):
    def test_equal_count_of_same_elements(self):
        self.assertItemsEqual([1,2,3], [1,2,3])

    def test_equal_count_of_different_elements(self):
        self.assertItemsEqual([1,2,3], [1,2,4])

    def test_different_count(self):
        self.assertItemsEqual([1,2,3], [1,2,3,4])
u.main()