def test():
    assert eval('1/2') == .5
    assert apply(eval, ('1/2',)) == .5