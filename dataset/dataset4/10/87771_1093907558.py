
def func(l):
    def get(i):
        return l[i]
    print(eval("(lambda x: get(x))(0)"))  # Call anonymous lambda with the constant 0 as argument
