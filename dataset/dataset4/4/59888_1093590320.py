class partial_applicable():
	def __call__(self, func):
		def __wrapper(*args, **kvargs):
			try:
				return func(*args, **kvargs)
			except TypeError:
				partial_func = partial(func, *args, **kvargs)
				return partial_applicable()(partial_func)

		return __wrapper