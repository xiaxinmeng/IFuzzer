
@given(x=strategies.integers())
def f(x):
    assert x >= 0
