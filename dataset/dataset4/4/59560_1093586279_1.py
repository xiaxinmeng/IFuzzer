test_gen(lambda g: g.__next__())
test_gen(lambda g: g.send(1))
test_gen(lambda g: g.throw(OSError))
test_gen(lambda g: g.close())