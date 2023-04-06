class A :
	def __init__(self) :
		self.__content = []
	def add(self, x) :
		self.__content.append(x)
	def __getattr__(self, attrname) :
		if string.upper(attrname) == "FIRST" :
			return self.__content[0]
		elif string.upper(attrname) == "LAST" :
			return self.__content[-1]