def func():
    a = 1
    b = 2
    c = 3

print("co_stacksize", func.__code__.co_stacksize)
print("co_nlocals", func.__code__.co_nlocals)