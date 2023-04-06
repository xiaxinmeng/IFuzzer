def _forward_A_reference():
    try:
        return a.A
    except AttributeError:
        # not yet..
        raise NameError('A')

class B:
    def spam(self: 'B', eggs: typing.Union['_forward_A_reference()', None]):
        pass