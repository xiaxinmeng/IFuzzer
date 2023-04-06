import copyreg
import types
import pickle
import sys

def picklemod(mod):
    if mod.__name__ in sys.modules:  # real modules
        return (__import__, (mod.__name__, None, None, ('',)))

    # module objects created manually:
    return (types.ModuleType, (mod.__name__,), mod.__dict__)
copyreg.pickle(types.ModuleType, picklemod)

pickle.loads(pickle.dumps(sys))  # works
import http.server
pickle.loads(pickle.dumps(http.server))  # works for nested modules

fakemod = types.ModuleType('fakemod')
fakemod.field1 = 'whatever'

# This fake type is used instead of types.ModuleType in order to re-confuse pickle back on track.
# Should not have been necessary in the first place,
# but types.ModuleType has misconfigured fields according to pickle
# (and they are read-only).
class _types_ModuleType(types.ModuleType):
    __module__ = 'types'
    __name__ = __qualname__ = 'ModuleType'

_orig_types_ModuleType = types.ModuleType
# bad monkey-patching, but needed for the confusion to work
types.ModuleType = _types_ModuleType
dump = pickle.dumps(fakemod)
# not necessary, but to show unpickling is regardless correct
types.ModuleType = _orig_types_ModuleType