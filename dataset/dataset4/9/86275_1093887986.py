@given(st.python_programs(), st.values())
def test_optimizer(func, arg):
    expected = func(arg)
    optimized = optimizer(func)(arg)
    assert optimized == expected