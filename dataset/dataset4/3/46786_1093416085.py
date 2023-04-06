def g():
    try:
        return g()
    except ValueError:
        return -1
self.assertRaises(RuntimeError, g)