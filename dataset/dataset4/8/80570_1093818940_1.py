import gc, _testcapi, sys

gc.enable_object_debugger(1)
x = _testcapi.corrupted_object()
y = []
y = None
# Debugger should trigger here
x = None