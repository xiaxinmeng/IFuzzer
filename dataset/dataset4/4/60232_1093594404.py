def fn1():
    while True:
        try:
            raise Exception()
        finally:
            pass
def fn2():
    while True:
        try:
            raise Exception()
        finally:
            break  # <-----
fn1()  # exception, as expected
fn2()  # silence!