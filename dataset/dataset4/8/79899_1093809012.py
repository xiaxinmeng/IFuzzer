from setuptools.command.build_py import build_py as _build_py

class build_py(_build_py):
    def initialize_options(self):
        _build_py.initialize_options(self)
        self.force = 1
        self.compile = 1

    def byte_compile(self, files):
        # self.compile == 1
        # self.force == None
        _build_py.byte_compile(self, files)
        # do stuff...