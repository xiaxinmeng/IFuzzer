def subgen():
	yield

def other_gen(self):
	move = yield from subgen()