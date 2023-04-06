import cPickle

res=[]
for x in range(1,2000):
    res.append(dict(doc=x, similar=[]))

cPickle.dumps(res)