import importlib
print('sys' in dir(importlib))  # True
from importlib import sys  # succeeds