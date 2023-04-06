from unittest import mock

class Foo:
    bar = None

patch = mock.patch.object(Foo, 'bar', 'x')
patch.start()
patch.stop()
patch.stop()