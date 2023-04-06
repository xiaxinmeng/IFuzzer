import cPickle
t = ('<s>', 'JOHN')
s1 = cPickle.dumps(t)
s2 = cPickle.dumps(cPickle.loads(cPickle.dumps(t)))
assert s1 == s2     # AssertionError