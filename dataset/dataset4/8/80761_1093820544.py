from unittest.mock import Mock

class Person:
    name: str
    age: int = 0

    def foo(self):
        pass

person_mock = Mock(spec=Person)
print(dir(Person))
print(dir(person_mock))
person_mock.foo
print("age" in dir(person_mock))
print("name" in dir(person_mock))