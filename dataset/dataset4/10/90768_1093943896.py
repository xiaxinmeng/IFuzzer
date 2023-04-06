self.assertRaises(self.failureException, self.assertCountEqual,
                          {'a': 1}, {'a': 2})