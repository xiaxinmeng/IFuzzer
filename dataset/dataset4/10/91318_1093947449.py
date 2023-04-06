
import importlib
import imp
spec = importlib.util.find_spec('_testmultiphase')
imp.load_dynamic("test.imp_dummy", spec.origin)
