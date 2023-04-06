# Not implemented formats. Ugly, but inevitable. This is the same as
# issue python/cpython#46783: equality is also used for membership testing and must
# return a result.
a = array.array('u', 'xyz')
v = memoryview(a)
self.assertNotEqual(v, a)
self.assertNotEqual(a, v)