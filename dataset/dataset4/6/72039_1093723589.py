from collections.abc import Iterable

def flatten_all(iterable):
    # -> 'one'
    # <- ['one']
    # -> ['one', [b'two', b'three'], ['four', ('five', (1, {'e', 'ee'}, (2, (3, ))), ['six'])], generator()]
    # <- ['one', b'two', b'three', 'four', 'five', 1, 'ee', 'e', 2, 3, 'six', 0, 1, 2]

    if isinstance(iterable, Iterable) and not isinstance(iterable, (str, bytes)):
        for it in iterable:
            yield from flatten_all(it)
    else:  # int & others types as is.
        yield iterable


if __name__ == "__main__":

    # Test Only
    def generator():
        for i in range(3):
            yield i

    a = ['one', [b'two', b'three'], ['four', ('five', (1, {'e', 'ee'}, (2, (3, ))), ['six'])], generator()]
    # a = 'one'
    # a = (True, False)

    print(list(flatten_all(a)))