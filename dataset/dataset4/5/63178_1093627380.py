class MethodRequest(request.Request):
	def __init__(self, *args, **kwargs):
		"""
		Construct a MethodRequest. Usage is the same as for
		`urllib.request.Request` except it also takes an optional `method`
		keyword argument. If supplied, `method` will be used instead of
		the default.
		"""
		if 'method' in kwargs:
			self.method = kwargs.pop('method')
		return request.Request.__init__(self, *args, **kwargs)

	def get_method(self):
		return getattr(self, 'method', request.Request.get_method(self))