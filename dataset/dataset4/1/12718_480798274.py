with self.assertRaises(OverflowError):
    a = [x for x in range(2**256)]