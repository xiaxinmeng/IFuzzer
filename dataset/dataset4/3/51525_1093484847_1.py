def outer(name):
    tmp = name
    def inner():
        print(tmp)
        tmp = "hello"
    return inner