
wr = weakref.ref(obj)
del obj
gc.collect()
self.assertIsNone(wr())
