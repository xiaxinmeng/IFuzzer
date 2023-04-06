class Foo:

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return False


class Bar:

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return True


assert Foo() not in {Bar(): 1}
