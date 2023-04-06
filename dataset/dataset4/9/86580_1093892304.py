@dataclass
class A:
    __field_doc__ = dict(num='number of widgets', total='total widgets')
    total: int
    num: int = 5
print(A.__doc__)