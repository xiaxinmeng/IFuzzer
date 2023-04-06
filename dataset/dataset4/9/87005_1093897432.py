import os
import sys
import importlib
import importlib.abc
import importlib.util
from unipath import Path # just an example

class DummyFinder(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.cwd = os.getcwd()
    def find_spec(self, fullname, path, target=None):
        if fullname == 'local':
            initpath = os.path.join(self.cwd, '__init__.py')
            if os.path.isfile(initpath):
                loader = importlib.machinery.SourceFileLoader(fullname, Path(initpath)) # some non-str Path-like object here
                return importlib.util.spec_from_file_location(fullname, initpath,
                        loader = loader, submodule_search_locations=[self.cwd])
        else:
            return None

sys.meta_path.append(DummyFinder())
importlib.import_module("local.test2")