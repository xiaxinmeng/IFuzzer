def test_shifted_true(self):
    self.assertEqual(True << 0, 1)
    self.assertEqual(True << 1, 2)