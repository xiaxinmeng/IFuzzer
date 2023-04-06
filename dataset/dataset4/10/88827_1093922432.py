class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

p = Person()
p.age = 10 # Now become faster