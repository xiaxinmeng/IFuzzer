import gc
t0ing0=object()
class A(object):
    def f():0
    x=t0ing0
r=gc.get_referrers(t0ing0)
if[0]:dct=r[0]
a=A
for i in range(1):a.f
dct["f"]=lambda:0
(a.f)