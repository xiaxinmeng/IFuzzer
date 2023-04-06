import _testcapi

def f():
    x = 1
    y = 2
    print(_testcapi.get_caller_locals())

f()