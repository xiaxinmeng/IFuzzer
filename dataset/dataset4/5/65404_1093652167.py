################################################################
import functools

def decorated(genfunc):
    @functools.wraps(genfunc)
    def wrapper(*args, **kargs):
        print('inside wrapper')
        for x in genfunc(*args, **kargs):
            yield 'decorated: {!r}'.format(x)
    print('outside wrapper')
    print('wrapper.__name__: {!r}'.format(wrapper.__name__))
    return wrapper

@decorated
def simple_genfunc():
    """Testdoc."""
    yield from range(10)

if __name__ == '__main__':
    print('simple_genfunc.__name__: {!r}'.format(
        simple_genfunc.__name__))
    print('simple_genfunc().__name__: {!r}'.format(
        simple_genfunc().__name__))
################################################################