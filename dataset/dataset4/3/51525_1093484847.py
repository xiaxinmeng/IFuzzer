def outer(name):
    tmp = name
    def inner():
        print(tmp)
    return inner

outer("foo") # prints "foo"