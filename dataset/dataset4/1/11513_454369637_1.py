
import _testcapi
def bug():
    _testcapi.raise_exception()
def func():
    bug()
func()
