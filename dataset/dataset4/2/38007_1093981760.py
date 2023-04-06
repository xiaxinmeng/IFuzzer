class FixGZip(gzip.GzipFile):
	"""the GzipFile class normally does not have an iterator; add one"""
	def __iter__(self):
		def stopIter():
			raise StopIteration
		while True:
			yield self.readline() or stopIter()