
# allocate ~4GB fragmented data
import numpy
a = [numpy.zeros(2**i, 'uint8') for i in range(1, 31)]
b = [numpy.zeros(131072, 'float64') for i in range(2048)]

# plot using TkAgg
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot
pyplot.plot()
pyplot.show()
