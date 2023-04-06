def foo():
    exec("attr = 1")
    a = locals()['attr']
    attr = 2 
foo()