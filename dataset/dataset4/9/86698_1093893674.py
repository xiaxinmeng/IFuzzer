class LogicInBool:
    def __bool__(self):
        print("In Bool!")
        return True

class SomeClass:
    def __init__(self):
        self.logic_in_bool = LogicInBool()

obj = SomeClass()
with unittest.mock.patch.object(obj, 'logic_in_bool', autospec=True):
    # "In Bool! is printed
    pass