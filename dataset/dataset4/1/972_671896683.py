import importlib.util

module_name = 'a'
path = os.getcwd() + '/a.py'
spec = importlib.util.spec_from_file_location(module_name, path)
module_a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module_a)
sys.modules[module_name ] = module_a