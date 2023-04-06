def __exit__(self, type_, value, tb):
        print('__exit__')           # print() is also built-in, but works
        print(sorted(builtins.__dict__.keys()))
        f = open('test.log', 'wt')  # <-- NameError: name 'open' is not defined
        f.close()