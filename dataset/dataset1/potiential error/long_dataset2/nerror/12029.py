caught_exceptions = ()
def f(to_raise):
    try:
       raise to_raise
    except caught_exceptions:
        print("Caught the exception")

f(Exception)
