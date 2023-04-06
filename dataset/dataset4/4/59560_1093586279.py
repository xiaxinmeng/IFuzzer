def test_gen(call_gen_method):
    def gen():
        call_gen_method(me)
        yield 1
    me = gen()