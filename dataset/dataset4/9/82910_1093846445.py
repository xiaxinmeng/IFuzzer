def decorator(m):
    return Wrapper(m)

class Wrapper(object):
    def __init__(self, method):
        self.method = method
        update_wrapper(self, method)

    def __call__(self, instance, *args, **kwargs):
        return self.__get__(instance, type(instance))(*args, **kwargs)

    def __get__(self, instance, owner):
        ... # do the wrapping