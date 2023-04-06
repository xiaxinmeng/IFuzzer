class InvalidHost(HTTPException):
	def __init__(self, host):
		self.host = host
	def __str__(self):
		return "invalid host- '%s'" % self.host