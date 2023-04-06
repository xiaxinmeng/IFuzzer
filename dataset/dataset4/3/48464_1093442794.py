if os.name == 'nt' and  sys.version_info >= (2,6):
    import distutils.msvc9compiler
    _orig_initialize = distutils.msvc9compiler.MSVCCompiler.initialize

    def _initialize(self, *args, **kw):
        rv = _orig_initialize(self, *args, **kw)
        try:
            self.ldflags_shared_debug.remove('/pdb:None')
        except ValueError:
            pass
        return rv

    distutils.msvc9compiler.MSVCCompiler.initialize = _initialize