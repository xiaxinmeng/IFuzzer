# --- script.py 
import types

class MyModule (types.ModuleType):
    __slots__ = (
        "_MyModule__a",
        "_MyModule__b",
    )

    def __init__(self, name):
        super().__init__(name)

m = MyModule("name")
# -- end of file