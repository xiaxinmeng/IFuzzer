def evil():
    loop.call_soon(evil)
    loop.stop()