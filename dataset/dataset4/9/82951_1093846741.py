from __future__ import print_function

import pickle, sys

class Foo:
    __name__ = __qualname__ = "Foo.ref"
    pass

Foo.ref = Foo

print(sys.version_info)

for proto in range(0, pickle.HIGHEST_PROTOCOL + 1):
    print("{}:".format(proto), end=" ")
    try:
        pkl = pickle.dumps(Foo, proto)
        print("Dump OK,", end=" ")
        assert(pickle.loads(pkl) is Foo)
        print("Load OK,")
    except Exception as err:
        print(repr(err))