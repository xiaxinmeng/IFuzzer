import weakref
class WeakMethod(object):
    def __init__(self, bound):
        self.weakself = weakref.proxy(bound.im_self)
        self.methodname = bound.im_func.func_name
    def __call__(self, *args, **kw):
        return getattr(self.weakself, self.methodname)(*args, **kw)