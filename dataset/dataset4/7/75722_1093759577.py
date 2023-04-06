class Something(object):
    def foobar(self):
        pass

    def foo(self):
        self.foobar()

    def bar(self):
        Something.foobar()  # this is broken


from unittest import mock
x = mock.Mock(spec=Something)
x.foo()
x.foo.assert_called_with()
x.bar()
x.bar.assert_called_with()  # this assertion pass!

# real code 
z = Something()
z.foo()
z.bar()  # raise exception