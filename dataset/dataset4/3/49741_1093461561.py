with nested(A, B, C) as (X, Y, Z):
    do_something()

with A as X:
    with B as Y:
        with C as Z:
            do_something()