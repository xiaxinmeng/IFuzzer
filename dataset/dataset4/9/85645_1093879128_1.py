import _testcapi
def foo():
#    _testcapi.meth_varargs()
    _testcapi.meth_fastcall()
def bar():
    foo()
bar()