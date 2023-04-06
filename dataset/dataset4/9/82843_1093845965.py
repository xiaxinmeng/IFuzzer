
def foo():
    try:
        raise Exception("returned")
    except Exception as e:
        print("except")
        return e.args[0]
    finally:
        print("finally")


print(foo())
