def my_decorator(func):
    return func

def my_awesome_function(*args, **kwargs):
    print(args)
    print(kwargs)

    return 42

my_awesome_function = my_decorator(my_awesome_function)