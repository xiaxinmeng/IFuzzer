def foo():
    try:
        1/0
    except Exception as err:
        import pdb; pdb.set_trace()
    x= 1

foo()