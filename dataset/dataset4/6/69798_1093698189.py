def main():
    try:
        raise MainError("Context inside generator")
    except MainError:
        yield  # __context__ could be changed to MainError

coro = main()
coro.send(None)
try:
    try: raise ValueError("Context outside of generator")
    except ValueError: raise SubError()
except SubError as ex:
    coro.throw(ex)  # __context__ is ValueError