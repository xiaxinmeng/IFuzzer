D = collections.deque(range(19999))
def test_func():
    try:
        D.remove("f")
    except:
        pass