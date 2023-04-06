# Why is this wrong?
def klammer(klammer_left,klammer_right):
    def klammer_decorator(func):
        def func_wrapper(name):
            return klammer_left + func(name) + klammer_right
        return func_wrapper
    return klammer_decorator