def test(n):
    return lambda fact: fact(fact, long(n))

test(8)
