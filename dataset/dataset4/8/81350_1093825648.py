# create an object, free its memory
obj = _testcapi.pyobject_freed()
# check that the object memory is freed
error = (_testcapi.pyobject_is_freed(obj) == False)