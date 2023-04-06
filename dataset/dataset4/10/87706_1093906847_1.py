if sys.version_info < (3, 5):
    import imp
    def load_dynamic(name, module_path):
        return imp.load_dynamic(name, module_path)
else:
    import importlib.util as _importlib_util
    def load_dynamic(name, module_path):
        spec = _importlib_util.spec_from_file_location(name, module_path)
        module = _importlib_util.module_from_spec(spec)
        # sys.modules[name] = module
        spec.loader.exec_module(module)
        return module