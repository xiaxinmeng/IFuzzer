reasonable_exp = 16
x *= 2 ** reasonable_exp
overflow_exp = int(math.log(sys.maxint, 2)) + 1 - reasonable_exp
self.assertRaises(MemoryError, x.__mul__, 2**overflow_exp)