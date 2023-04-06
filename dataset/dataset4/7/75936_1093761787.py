# Create a dict and a set
d = {1: '1'}
s = {1}

# They have different types
print(type(d))             # <type 'dict'>
print(type(s))             # <type 'set'>
print(type(d) is type(s))  # False
print(type(s) is type(d))  # False
print(type(d) == type(s))  # False