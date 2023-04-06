
class C:
    a: " ClassVar[int]" = 3
get_type_hints(C, globals())  # SyntaxError: Forward reference must be an expression -- got ' ClassVar[int]'

