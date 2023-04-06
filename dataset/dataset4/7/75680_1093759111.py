def test_issue31499(self):
    def test():
        ...
    test()
    test.support.gc_collect()