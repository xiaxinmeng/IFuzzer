def deco2(f):
    return f

def go():
    f = 5
    f = (
        deco1(
            deco2(
                f
            )
        )
    )


import trace
tracer = trace.Trace(count=1,trace=0,countfuncs=0, countcallers=0)
tracer.run('go()')
for k,v in  tracer.results().counts.items():
    print(k,v)