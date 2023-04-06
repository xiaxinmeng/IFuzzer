from typing import Callable, Any


def classproperty(method):
	"""A decorator adding properties to classes."""

	class ClassPropertyDescriptor:
		"""A descriptor for class properties.."""

		_name: str
		_getter: Callable
		_setter: Callable
		_deleter: Callable

		def __init__(self, getter: Callable = None, setter: Callable = None, deleter: Callable = None, doc: str = None):
			self._getter = getter
			self._setter = setter
			self._deleter = deleter
			self._name = ''

			if doc is None and getter is not None:
				doc = getter.__doc__
			self.__doc__ = doc

		def __set_name__(self, owner: Any, name: str):
			self._name = name

		def __get__(self, instance: Any, objtype: type = None):
			if self._getter is None:
				raise AttributeError(f'unreadable attribute {self._name}')

			return self #._getter(objtype)

		def __set__(self, instance: Any, value: Any):
			print(f"__set__: {value}")
			if self._setter is None:
				raise AttributeError(f"can't set attribute {self._name}")

			self._setter(instance, value)

		def __delete__(self, instance: Any):
			if self._deleter is None:
				raise AttributeError(f"can't delete attribute {self._name}")

			self._deleter(type(instance))

		def getter(self, getter: Callable):
			prop = type(self)(getter, self._setter, self._deleter, self.__doc__)
			prop._name = self._name

			return prop

		def setter(self, setter: Callable):
			prop = type(self)(self._getter, setter, self._deleter, self.__doc__)
			prop._name = self._name

			print(f"setter: self: {id(self)}; prop:{id(prop)}")
			return prop

		def deleter(self, deleter: Callable):
			prop = type(self)(self._getter, self._setter, deleter, self.__doc__)
			prop._name = self._name

			return prop

	return ClassPropertyDescriptor(method)


class TestClass:
	_member: int = 1

	@classproperty
	def Member(cls) -> int:
		"""Class_1.Member"""
		return cls._member

	@Member.setter
	def Member(cls, value: int) -> None:
		print(f"value: {value} {cls} {id(cls)}")
		cls._member = value


def main():
	print(f"TestClass.Member: {TestClass.Member}   {id(TestClass.Member)}")

	TestClass.Member.__set__(TestClass, 12)
	TestClass.Member = 13
	TestClass.Member.__set__(TestClass, 14)
	print(f"TestClass.Member: {TestClass.Member}   {id(TestClass.Member)}")


if __name__ == "__main__":
	main()