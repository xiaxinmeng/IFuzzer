def test(obj):
    try:
        type(obj).__getattribute__(obj, (1,))
    except AttributeError as e:
        print(e)
class C:
    pass
test(str)
test(C)
test(C())