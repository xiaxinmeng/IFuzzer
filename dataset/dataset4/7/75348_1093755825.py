import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
for i in range(1):
    lst=[str()]
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
    del a
    while lst:keepali0e.append(lst[:])