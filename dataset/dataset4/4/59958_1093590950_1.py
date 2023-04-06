class A:
    def f(*all_positional, **all_keywords):
        print(super(A, all_positional[0]).__repr__())