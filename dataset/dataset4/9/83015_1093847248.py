class A(typing.TypedDict):
    a: int  # a is required

class B(A, total=False):
    b: bool  # a is required, b is optional

class C(B):
    c: str  # a is required, b is optional, c is required again