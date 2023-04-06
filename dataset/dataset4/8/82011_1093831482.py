import contextlib
def simple():
    with contextlib.nullcontext():
        for number in range(2):
            try:
                return number
            finally:
                break

simple()