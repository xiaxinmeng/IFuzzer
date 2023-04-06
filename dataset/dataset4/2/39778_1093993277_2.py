x = 1
def __gen_wrapper():
    _[x] = x # variable capture here
    def __gen():
        for i in range(10):
            yield _[x]
    return __gen()

g = __gen_wrapper()