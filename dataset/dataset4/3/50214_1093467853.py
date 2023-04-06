def test_set_literal(self):
    s = set([1,2,3])
    t = {1,2,3}
    self.assertEqual(s, t)