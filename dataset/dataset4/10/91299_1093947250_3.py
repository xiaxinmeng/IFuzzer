class MyClass:
    def who_am_i(self):
        cls = __class__
        print(cls)
        if cls is not self.__class__:
            raise Exception(f"closure lies: __class__={cls} {self.__class__=}")

def copy_class(cls, new_name):
    cls_dict = cls.__dict__.copy()
    # hack the dict to modify the class copy
    return type(cls)(new_name, cls.__bases__, cls_dict)


MyClass().who_am_i()
MyClass2 = copy_class(MyClass, "MyClass2")
MyClass2().who_am_i()