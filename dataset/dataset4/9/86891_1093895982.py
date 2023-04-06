def foo():
    outer_var = 1

    def bar():
        inner_var: outer_var = T
    
    return bar

inner = foo()
print(inner.__closure__)