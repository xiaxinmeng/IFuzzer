from __future__ import annotations
import dataclasses
from some_library_typing import mytype
from some_library_module_a import MyClass

inst = MyClass('bar')

for f in dataclasses.fields(inst):
    if f.type is mytype:
        print('mytype found')
        break
else:
    print('mytype not found')