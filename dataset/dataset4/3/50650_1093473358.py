import sys

module = __import__("broken_module")
instance = module.TestClass()
print("a: "+str(instance.test()))
del sys.modules["broken_module"]
print("b: "+str(instance.test()))
del module
print("c: "+str(instance.test()))