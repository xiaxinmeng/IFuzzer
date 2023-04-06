
class Z(object):
    def __str__(self):
        raise ValueError('Z error')


def raise_generator():
    yield 'three values are: %s %s %s' % (
        'primeiro',
        Z(),  # traceback must point to this lineno 9
        'terceiro'  # but points to this lineno 10 (__str__ only, __eq__ is OK)
    )


print(list(raise_generator()))
