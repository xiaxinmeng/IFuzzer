import json, timeit
obj = [[1,2,3]*10]*10
class writable(object):
	def write(self, buf): pass
w = writable()
print('dumps: %.3f' % timeit.timeit(lambda: json.dumps(obj), number=10000))
print('dump:  %.3f' % timeit.timeit(lambda: json.dump(obj,w), number=10000))