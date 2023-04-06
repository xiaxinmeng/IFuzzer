def func(x):
    try:
        x + 0
    except (ValueError, TypeError):
        raise MyException.no_context('x is not a number')
    do_something_with(x)