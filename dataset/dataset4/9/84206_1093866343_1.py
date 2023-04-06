class F(Enum):
	def _generate_next_value_(name, *args):
		return name
	A = auto()
	B = auto()
	
	
F.B.value  # Returns 'B', as intended