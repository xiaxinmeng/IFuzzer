p = Packer()
p.pack_int('foo')  # should raise a TypeError
p.pack_int(2**100) # should raise a ValueError