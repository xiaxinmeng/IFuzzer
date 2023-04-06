from functools import partial

class partial_applicable():
	def __call__(self, func):
		def __wrapper(*args, **kvargs):
			try:
				return func(*args, **kvargs)
			except TypeError:
				return partial(func, *args, **kvargs)

		return __wrapper