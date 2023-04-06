
class TypeVar:
    def __init__(self, name, *constraints):
        # in actual TypeVar, each constraint is run through
        # typing._type_check, casuing TypeError via not callable() 
        print(repr(constraints))

class V(TypeVar("T")):
    pass
