
from dataclasses import field, dataclass, asdict, fields


def string_check(x):
    if type(x) != str:
        raise ValueError("Should be a string.")
    return x


def validator_factory(field_name, validator):
    def fget(self):
        return self.__dict__[field_name]

    def fset(self, value):
        self.__dict__[field_name] = validator(value)

    return property(fget, fset)


@dataclass
class MyClass():
    my_value: str = validator_factory("my_value", string_check)


@dataclass
class ClassSchema():
    field_defaults: list


my_class_schema = ClassSchema(
    field_defaults=[f.default for f in fields(MyClass)]
)

print(my_class_schema)
print(asdict(my_class_schema))
