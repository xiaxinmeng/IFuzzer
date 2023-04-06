def f() -> List['int']:
    ...

assert get_type_hints(f)['return'] == List[int]