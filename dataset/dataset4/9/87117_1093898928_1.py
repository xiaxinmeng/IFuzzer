def foo():
    try:
        print("a")
        foo()
    except:
        print("b")
        foo()

foo()