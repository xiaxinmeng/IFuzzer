import time
import itertools


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def new_pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    return zip(iterable, iterable[1:])


combine = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


if __name__ == '__main__':
    start_time = time.time()

    # Current
    print('Current:')
    print(list(pairwise(combine)))
    # output: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]

    print()

    # New
    print('New:')
    print(list(new_pairwise(combine)))
    # output: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]