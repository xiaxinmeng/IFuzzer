class Game(object):
	def __init__(self):
		self.gen = self.first_gen()
		next(self.gen)
	def first_gen(self):
		while True:
			from generators import \
				other_gen
			yield from other_gen(self)