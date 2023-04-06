if __debug__:
    self.assertEqual(opt, 0)
elif ValuesTestCase.__doc__ is not None:
    self.assertEqual(opt, 1)