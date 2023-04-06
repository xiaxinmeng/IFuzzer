import _testcapi
def f(): yield _testcapi.stack_pointer()
print(_testcapi.stack_pointer() - next(f()))