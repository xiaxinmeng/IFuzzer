m1 = example.message()
m1.f1 = 6.21.as_32_bit_float() # Does the precision truncation upfront
b = m.encode() # uses struct pack
m2 = example.message(b) # uses struct unpack
if m1 != m2:  # rich comparison
  print('fail')