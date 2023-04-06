import operator

a=[1,2]
b=["x","y"]

reduce(operator.add, [a,b])
# Works, gives "[1, 2, 'x', 'y']" as expected.