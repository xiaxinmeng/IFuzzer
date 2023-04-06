#init.py
__all__ = ['second', 'first']
print('i\'m starting the directory')

#first.py
print('hi, i\'m the first')
from . import second

#second.py
print('hi, i\'m the second')
from . import first