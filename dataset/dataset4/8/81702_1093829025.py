
name = 'testext'

spec = importlib.util.find_spec(name)
print(name in sys.modules)
module = importlib.util.module_from_spec(spec)
print(name in sys.modules)
spec.loader.exec_module(module)
print(name in sys.modules)
