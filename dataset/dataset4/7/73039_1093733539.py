def foo():
    # Function block
    print(locals())

class Bar:
    # Class block
    print(locals())

# Module level
print(locals())