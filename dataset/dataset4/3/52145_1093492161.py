@sweepargs(arg=range(5))
def test_sweepargs_demo(arg):
    ok_(arg < 5)
    ok_(arg < 3)
    ok_(arg < 2)