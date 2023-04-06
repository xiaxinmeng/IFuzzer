def my_type(string):
    if string not in ['a', 'b', 'c']:
        raise TypeError
    return string