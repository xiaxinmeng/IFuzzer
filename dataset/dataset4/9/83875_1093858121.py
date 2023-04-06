import collections

class str2(str):
    def format(self, *args, **kwargs):
        return super().format(*args, **kwargs)

def unpacknonekey(s):
    print('input:', type(s), s)
    try:
        print('str key:', s.format(**{'bar': 'qux'}))
        print('none key:', s.format(**{'bar': 'qux', None: ''}))
    except TypeError as e:
        print('error:', e)

template = 'foo {bar} baz'
unpacknonekey(template)
unpacknonekey(str2(template))
unpacknonekey(collections.UserString(template))