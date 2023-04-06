from collections.abc import Mapping
from dataclasses import dataclass, fields, _FIELDS, _FIELD

class DataclassMappingMixin(Mapping):
    def __iter__(self):
        return (f.name for f in fields(self))

    def __getitem__(self, key):
        field = getattr(self, _FIELDS)[key]
        if field._field_type is not _FIELD:
            raise KeyError(f"'{key}' is not a dataclass field.")
        return getattr(self, field.name)

    def __len__(self):
        return len(fields(self))


@dataclass
class MyDataclass(DataclassMappingMixin):
    a: int = 1
    b: int = 2


my_dataclass = MyDataclass(a='3')
print(my_dataclass.__class__.__mro__)
print(my_dataclass.__class__.__name__)
print(my_dataclass['a'])
print(my_dataclass['b'])
print(dict(my_dataclass))
print(dict(**my_dataclass))
print(fields(my_dataclass))