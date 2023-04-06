import sys

def tracefunc(frame, event, arg):
    if event == "call":        
        print('frame.f_locals.items: ->', frame.f_locals.items())
    return tracefunc

sys.setprofile(tracefunc)


def test_sum(x: int, y: int):
    return x + y

test_sum(10, 20)

import asyncio