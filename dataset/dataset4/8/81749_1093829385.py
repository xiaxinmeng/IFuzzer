a = 1
def func():
    print(a)  # refers to global a
    a = a + 1  # make a new local 'a'