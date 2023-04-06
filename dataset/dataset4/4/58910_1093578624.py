for expr in [False, None, True, 1, 0]:  # add the rest
   self.assertEqual(bool(expr), getargs_p(expr))