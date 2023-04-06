from asyncio import CancelledError

cancelled = False

def coro():
    global cancelled
    print(1)
    yield (1,)
    print("cancel")
    cancelled = True
    #print(2)
    #yield (2,)  # uncomment this line makes cancel success.

c = coro()

while True:
    try:
        if cancelled:
            r = c.throw(CancelledError)
        else:
            r = c.send(None)
    except StopIteration:
        print("end")
        break
    except CancelledError:
        print("cancelled")
        break