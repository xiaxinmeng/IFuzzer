
# the global `__name__` is normally the module's name.
__name__ = "something"

class Meta_default_prepare(type):
    def __new__(meta, name, bases, ns):
        print("ns for", name, "\n   ", ns)
        return super().__new__(meta, name, bases, ns)

class Meta_custom_prepare(Meta_default_prepare):
    def __prepare__(meta, *args):
        return {'__name__': 'another_name'}

class Spam(metaclass=Meta_default_prepare):
    pass

class Eggs(metaclass=Meta_custom_prepare):
    pass

print("Spam module and name:", Spam.__module__, Spam.__name__)
print("Eggs module and name:", Eggs.__module__, Eggs.__name__)

