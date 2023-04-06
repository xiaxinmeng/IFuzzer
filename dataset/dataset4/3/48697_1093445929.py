def foo():
    x = 1
    exec("x = 42")
    print(x)    # Prints 1  (exec has no effect)