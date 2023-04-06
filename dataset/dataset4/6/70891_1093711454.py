from unittest import mock

class C(object):
    def f(self):
        pass

c = C()

with mock.patch.object(c, 'f', autospec=True):
    with mock.patch.object(c, 'f', autospec=True):
        pass