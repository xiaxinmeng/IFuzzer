# context manager "query" (open in init, yield rows and close on exit)
class _query():
    def __init__(self, **kwargs):
        pass

    def __enter__(self):
        return [1, 2, 3]

    def __exit__(self, type_, value, tb):
        print('__exit__')           # print() is also built-in, but works
        f = open('test.log', 'wt')  # <-- NameError: name 'open' is not defined
        f.close()


# this works fine
def a():
    try:
        raise Exception('volatile exception')
    except Exception as e:
        raise e


# this does not work
def b():
    try:
        raise Exception('stored exception')
    except Exception as e:
        ee = e  # <-- storing exception and then
    raise ee    # <-- re-raising stored exception triggers the issue


def event_gen(**kwargs):
    with _query() as cursor:
        for _ in cursor:
            yield b     # <--- does not work
            # yield a   # <--- works fine


def run(**kwargs):
    g = event_gen(**kwargs)
    r = next(g)
    r()
    # This also works
    # for r in event_gen(**kwargs):
    #     r()

if __name__ == '__main__':
    run()