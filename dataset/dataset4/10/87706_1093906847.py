if sys.version_info[:2] < (3, 3):
    import imp
    def load_dynamic(name, module_path):
        return imp.load_dynamic(name, module_path)
else:
    from importlib.machinery import ExtensionFileLoader
    def load_dynamic(name, module_path):
        return ExtensionFileLoader(name, module_path).load_module()