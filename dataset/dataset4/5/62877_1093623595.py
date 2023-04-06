import contextlib


@contextlib.contextmanager
def nested_delayed(*callables):
	"""
	Instantiate and invoke context managers in a nested way.  each argument is a callable which
	returns an instantiated context manager
	"""
	if len(callables) > 1:
		with nested_delayed(*callables[:-1]) as a, callables[-1]() as b:
			yield a + (b,)
	elif len(callables) == 1:
		with callables[0]() as a:
			yield (a,)
	else:
		yield ()


def nested(*managers):
	"""
	Invoke preinstantiated context managers in a nested way
	"""
	def helper(m):
		"""
		A helper that returns the preinstantiated context manager when invoked
		"""
		def callable():
			return m
		return callable
	return nested_delayed(*(helper(m) for m in managers))



@contextlib.contextmanager
def ca():
	print("a")
	yield 1

class cb:
	def __init__(self):
		print ("instantiating b")
	def __enter__(self):
		print ("b")
		return 2
	def __exit__(*args):
		pass

@contextlib.contextmanager
def cc():
	print("c")
	yield 3


combo = nested(ca(), cb(), cc())
combo2 = nested_delayed(ca, cb, cc)

with combo as a:
	print("nested", a)

with combo2 as a:
	print("nested_delayed", a)

with ca() as a, cb() as b, cc() as c:
	print ("syntax", (a, b, c))