
a = np.array([[0, 1, 2], [3, 4, 5]])
mv = memoryview(a.T)
mv.f_contiguous 
# True
mv.cast('i', (3, 2))
# TypeError: memoryview: casts are restricted to C-contiguous views
