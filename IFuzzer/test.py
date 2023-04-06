import weakref
def test_proxy_iter():
	class MyObj:
		def __iter__(obj_1):
			return obj
	
	obj = weakref.proxy(TypeError)
	obj_1 = MyObj()
	try:
		"bench" in obj_1
	except TypeError:
		pass
test_proxy_iter()
