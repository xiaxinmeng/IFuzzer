class BadRepr:
	def __repr__(self):
		1/0
def broken():
    x=BadRepr()
    x=x #filler line for debugger