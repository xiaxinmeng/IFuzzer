with StringIO() as test:
    test.write("hi!")
    return test.getvalue()