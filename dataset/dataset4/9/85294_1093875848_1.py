
class NegatorTwo:
    @singledispatchmethod
    def neg(arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    def _(self, arg: int):
        return -arg

    @neg.register
    def _test(self, arg: bool):
        return not arg


if __name__ == "__main__":

    n = NegatorTwo()
    print(n.neg(0))
    print(n.neg(False))
    print(n.neg(arg=0))

