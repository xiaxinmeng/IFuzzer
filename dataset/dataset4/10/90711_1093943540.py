
class C:
    a: "ClassVar"

get_type_hints(C, globals())  # TypeError: Plain typing.ClassVar is not valid as type argument
