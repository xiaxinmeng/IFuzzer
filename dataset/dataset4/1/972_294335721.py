
moduleName = 'testmodule'
path = os.getcwd() + '/testmodule.py'
spec = importlib.util.spec_from_file_location(moduleName, path)
module_test = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module_test)
sys.modules[moduleName] = module_test
with self.assertRaises(ModuleNotFoundError):
    importlib.reload(sys.modules[moduleName])
