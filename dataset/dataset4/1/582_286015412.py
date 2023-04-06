
def check_sorted(L):
    for i in range(len(L)-1):
        assert(L[i+1] >= L[i])

lists = []

lists.append(['z','ab','cad','_ag'])
lists.append(['z','ab','cad','_ag','\uffff'])
lists.append([1,-1,5])
lists.append([1,-1,5,2**60,-2**60])
lists.append([1.1,-1.1,0])
lists.append([1,1.1,5,-2,0.5])
lists.append([b'sdf',b'afd',b'153d'])
lists.append([(),(1,),(2,)])

for l in lists.copy():
    lists.append([(x,1.1,-4,'a') for x in l])
    lists.append([((x,1.1,-4,'a'),42) for x in l])

for l in lists:
    check_sorted(sorted(l))

try:
    sorted(['a',1])
except TypeError:
    pass
