class Base(object):
    def mymethod(self, myonlyarg='hello world'):
        assert not hasattr(super(Base, self), 'mymethod')