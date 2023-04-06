import unittest as u
class Test(u.TestCase):
    def test_Count(self):
        self.assertItemsEqual([1,2,3], [1,2,4])
u.main()