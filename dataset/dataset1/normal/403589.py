def outer(*args):
    def inner():
       print(args)

outer(1,2,3)
