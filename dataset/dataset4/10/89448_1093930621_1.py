print(type(x.a))
# Prints <class 'bytes'> ???  Both mypy and PyRight agree that x.a is a c_char.

some_variable = pointer(x.a)
# Traceback (most recent call last):
#   File "C:\Users\cires\ctypes_test.py", line 23, in <module>
#     some_variable = pointer(x.a)
# TypeError: _type_ must have storage info