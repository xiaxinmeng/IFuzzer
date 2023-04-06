from time import sleep
from abc import ABC, ABCMeta, abstractmethod

class MyMetaClass(ABCMeta):
    @classmethod
    @property
    def expensive_metaclass_property(cls):
        """This may take a while to compute!"""
        print("computing metaclass property"); sleep(3)
        return "Phew, that was a lot of work!"

    
class MyBaseClass(ABC, metaclass=MyMetaClass):
    @classmethod
    @property
    def expensive_class_property(cls):
        """This may take a while to compute!"""
        print("computing class property .."); sleep(3)
        return "Phew, that was a lot of work!"
    
    @property
    def expensive_instance_property(self):
        """This may take a while to compute!"""
        print("computing instance property ..."); sleep(3)
        return "Phew, that was a lot of work!"

class MyClass(MyBaseClass):
    """Some subclass of MyBaseClass"""
    
help(MyClass)