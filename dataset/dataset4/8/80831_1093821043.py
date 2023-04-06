
import functools


def method_cache(method):
	def wrapper(self, *args, **kwargs):
		# it's the first call, replace the method with a cached, bound method
		bound_method = functools.partial(method, self)
		cached_method = functools.lru_cache()(bound_method)
		setattr(self, method.__name__, cached_method)
		return cached_method(*args, **kwargs)
	return wrapper


class MyClass:
	calls = 0

	@method_cache
	def call_me_maybe(self, number):
		self.calls += 1
		return number


ob = MyClass()
ob.call_me_maybe(0)
ob.call_me_maybe(0)
assert ob.calls == 1
