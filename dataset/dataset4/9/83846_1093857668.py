class Meta(type):
	def mro(cls):
		return type.mro(cls)[1:]
class X(metaclass=Meta):
	    pass