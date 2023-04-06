from enum import Enum, auto

class E(Enum):
	A = auto()
	B = auto()
	def _generate_next_value_(name, *args):
		return name

for l in (E):
	print(l.name)
	print(l.value)