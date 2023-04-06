class T(NamedTuple):
    field: str = None
print(get_type_hints(T))