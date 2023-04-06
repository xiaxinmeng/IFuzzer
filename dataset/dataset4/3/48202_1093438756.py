from gc import collect
import _lsprof

def callMethod(obj):
    obj.clear()
    collect()

obj = _lsprof.Profiler()
obj.enable()
callMethod(obj)
obj.enable()