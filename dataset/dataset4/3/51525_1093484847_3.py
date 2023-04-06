def outer(name):
    tmp = name
    def inner():
        tmp = "hello"
        print(tmp)
    return inner