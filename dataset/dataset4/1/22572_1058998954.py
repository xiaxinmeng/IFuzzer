import dataclasses
from unittest.mock import Mock

class Person:

    def __init__(self, name):
        self.name = name
    
m_instance = Mock(spec=Person("Jim"))
print(m_instance.name)


m_class = Mock(spec=Person)
print(m_class.name)