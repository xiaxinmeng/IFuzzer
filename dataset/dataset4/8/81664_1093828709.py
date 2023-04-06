from _testcapi import stack_pointer
class D(dict):
    def __missing__(self, key):
        sp = stack_pointer()
        print(f"stack usage = {TOP - sp}")
        return None
d = D()
TOP = stack_pointer()
d[0]