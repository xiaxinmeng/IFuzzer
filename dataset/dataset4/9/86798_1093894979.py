def foo():
    try:
        1/0
    except ZeroDivisionError as e:
       	ZeroDivisionError = 1
foo()