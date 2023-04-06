m1 = example.message()
m1.f1 = 6.21
b = m.encode() # uses struct pack
m2 = example.message(b) # uses struct unpack
if m1 != m2:  # rich comparison
  print('fail')