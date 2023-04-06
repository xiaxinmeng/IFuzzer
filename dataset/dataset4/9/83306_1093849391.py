class Foo:
    @property
    def bar(self) -> int:
        '''Bar docs for property'''
        return 42

    @bar.setter
    def bar(self, value: int) -> None:
        '''Bar docs for setter'''
        pass

help(Foo.bar)