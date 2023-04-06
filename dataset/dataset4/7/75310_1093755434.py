import abc

class Foo(list, metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def abstract(self):
		pass

Foo()