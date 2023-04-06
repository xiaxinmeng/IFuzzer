class A:
    @cached_property
    def x(self):
        print('!')
        return 42