def add_annotation(cls, v, t):
    if not "__annotations__" in cls.__dict__:
        # Doesn't exist, add it.
        cls.__annotations__ = {}
    cls.__annotations__[v] = t

add_annotation(Base, 'a', int)
add_annotation(Alpha,'a',  float)
add_annotation(Beta, 'a', str)