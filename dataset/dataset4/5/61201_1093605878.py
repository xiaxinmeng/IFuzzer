class MyTest(unittest.TestCase):

    def test_b(self):
        """some test"""
        for i in range(2, 5):
            for j in range(0, 3):
                with self.subTest(i=i, j=j):
                    self.assertNotEqual(i % 3, j)