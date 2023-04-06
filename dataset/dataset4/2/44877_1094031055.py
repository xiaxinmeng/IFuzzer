x = [0,0,0,0]
self.assertRaises(MemoryError, x.__mul__, sys.maxint/2+1)
self.assertRaises(MemoryError, x.__imul__, sys.maxint/2+1)