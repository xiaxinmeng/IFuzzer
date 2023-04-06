from _testcapi import stack_pointer

class D(dict):
    def items(self):
        sp = stack_pointer()
        print(f"stack used: {TOP - sp}")
        return []

mappingproxy = type(object.__dict__)
p = mappingproxy(D())
TOP = stack_pointer()
p.items()