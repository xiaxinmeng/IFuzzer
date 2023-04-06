class mydecorator(classmethod):
    def __set_name__(self, type, name):
        atexit.register(self.__func__, type)

class Program:
    @mydecorator
    def clean_up(cls):
        ...