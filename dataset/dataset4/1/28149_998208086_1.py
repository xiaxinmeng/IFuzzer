
class Retry(Exception):
    pass


def x():
    i = 0
    while True:
        try:
            i += 1
            try:
                return i
            finally:
                if i < 10:
                    raise Retry()  # simulate failed cleanup or something
        except Retry:
            pass


print('x', x())  # prints 10
