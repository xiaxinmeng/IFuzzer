import builtins
from importlib.machinery import PathFinder
import importlib
import sys
import _imp
from functools import partial
def copy_module(module):
    new = type(sys)(module.__name__)
    new.__dict__.update(module.__dict__)
    return new
_absent = object()
def new_exec(code, globals=_absent, locals=_absent, *, new_builtins):
    if globals == _absent:
        frame = sys._getframe(2)
        globals = frame.f_globals
        locals = frame.f_locals
    elif locals == _absent:
        locals = globals
    globals.setdefault("__builtins__", new_builtins);
    return exec(code, globals, locals)
dct={}
dct["__builtins__"] = b = copy_module(builtins)
b.exec = partial(new_exec, new_builtins=b)
spec = PathFinder.find_spec("_bootstrap",importlib.__path__)
source_bootstrap = type(sys)("_bootstrap");
spec.loader.exec_module(source_bootstrap);
external_spec = PathFinder.find_spec("_bootstrap_external",importlib.__path__)
source_bootstrap_external = type(sys)("_bootstrap_external");
external_spec.loader.exec_module(source_bootstrap_external);
source_bootstrap.__name__ = "importlib._bootstrap";
source_bootstrap_external.__name__ = "importlib._bootstrap_external";
new_sys = copy_module(sys)
new_sys.path_importer_cache = {}
new_sys.path_hooks = []
new_sys.meta_path = []
new_sys.modules = {
                    "importlib._bootstrap":source_bootstrap,
                    "importlib._bootstrap_external":source_bootstrap_external,
                  }
for mod in new_sys.modules.values():
    mod.__builtins__ = b
b.__import__ = source_bootstrap.__import__
source_bootstrap._install(new_sys,_imp)
exec("import _pickle", dct)