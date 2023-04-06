a = bytearray(10)
size = sys.getsizeof(a)
a.pop()  # Defeat expanding buffer off-by-one quirk
self.assertEqual(sys.getsizeof(a), size, "Quirk not defeated")
del a[:1]
# Or a.pop(0)  # Does not trigger bug
# Or a[:1] = ()  # Triggers bug
self.assertEqual(sys.getsizeof(a), size, "Test assumes buffer not resized")
a += bytes(2)  # Add exactly the number of free bytes in buffer
# Or a.extend(bytes(2))  # Unaffected
# Or a.append(0); a.append(0)  # Unaffected
# Or a[8:] = bytes(2)  # Unaffected
del a  # Trigger memory buffer to be freed, with verification