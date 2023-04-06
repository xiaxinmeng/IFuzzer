if case == 2:
    _bootstrap = type(sys)("_bootstrap")
    _bootstrap._weakref = sys.modules['_weakref']

    class ModuleSpec:
        @staticmethod
        def method():
            pass

    spec = ModuleSpec()
    spec.name = "_weakref"

    module = _imp.create_builtin(spec)
    module.__spec__ = spec