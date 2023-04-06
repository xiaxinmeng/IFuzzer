
class Meta(type):
    #
    def __new__(mcls, name, bases, namespace, **kwds):
        # create new class, which will call __init_subclass__ and __set_name__
        new_class = type.__new__(mcls, name, bases, namespace, **kwds)
        # finish setting up class
        new_class.some_attr = 9
