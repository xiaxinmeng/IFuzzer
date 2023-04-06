import pickle
print("begin")
#a = numpy.zeros((2.5e9 / 8,), dtype = numpy.float64)
a = ('a' * (2 ** 31))
print("allocated")
#print(a);
pickle.dumps(a, pickle.DEFAULT_PROTOCOL)
print("end")