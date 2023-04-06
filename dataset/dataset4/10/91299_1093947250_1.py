class MyClass:
    def hello(self):
        print("Hello", self.__class__)

def copy_class(cls, new_name):
    cls_dict = cls.__dict__.copy()
    # hack the dict to modify the class copy
    return type(cls)(new_name, cls.__bases__, cls_dict)

MyClass2 = copy_class(MyClass, "MyClass2")
MyClass2().hello()