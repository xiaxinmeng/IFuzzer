import typing
  
def f(clazz, ns):
    """
    >>> class MyClass:
    ...   my_field: 'MyClass'
    >>> f(MyClass, globals())
    """
    typing.get_type_hints(clazz, ns)