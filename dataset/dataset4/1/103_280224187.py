class AlwaysAttributeError:
            def __getattr__(self, _):
                raise AttributeError

module_name = 'test_from_import_AttributeError'
self.addCleanup(unload, module_name)
sys.modules[module_name] = AlwaysAttributeError()