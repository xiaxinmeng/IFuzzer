def simple_test():
    spam = Spam()
    assert spam.get_next() == 1
    try:
        spam.get_next()
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError
    assert spam.get_next() == 3
    print("simple test passed")

simple_test()