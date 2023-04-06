
class K:
    def __eq__(self, other):
        return True
    def __hash__(self):
        time.sleep(10)
        return 42

d1 = {"foo": 1, "bar": 2, "baz": 3, K(): 4}
d2 = dict(**d1)
