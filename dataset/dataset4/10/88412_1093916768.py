import importlib.metadata
print('looks like a list:')
print(importlib.metadata.distribution('pip').entry_points)
print('first item:')
print(importlib.metadata.distribution('pip').entry_points[0])