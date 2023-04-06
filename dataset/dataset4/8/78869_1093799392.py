
import pandas
import numpy

now = pandas.Timestamp.now()
arr = numpy.array([ ['a', now] for i in range(0, 3)])
arr.sum(0)
