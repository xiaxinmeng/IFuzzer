import abc


class Base(abc.ABC):
    @abc.abstractclassmethod
    def abstract_class(cls):
        pass

    @abc.abstractstaticmethod
    def abstract_static():
        pass

    @abc.abstractproperty
    def abstract_property(self):
        pass


class Child(Base):
    @classmethod
    def abstract_class(cls):
        print('Abstract class method')

    @staticmethod
    def abstract_static():
        print('Abstract static method')

    @property
    def abstract_property(self):
        return 'Abstract property'


child = Child()
child.abstract_class()
child.abstract_static()
print(child.abstract_property)