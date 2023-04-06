import pickle
a = bytearray(range(255)) #bytes containing 0..255
b = bytes(a)
c = pickle.dumps(b,protocol=0)
print(c)#human readable in 2, not in 3
c.decode('ascii')#throws in 3, not in 2