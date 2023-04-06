import _testcapi
class C(): pass
_testcapi.set_nomemory(0, 5)
C()
