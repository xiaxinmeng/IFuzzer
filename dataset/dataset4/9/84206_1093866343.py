from enum import Enum, auto

class E(Enum):
	A = auto()
	B = auto()
	def _generate_next_value_(name, *args):
		return name