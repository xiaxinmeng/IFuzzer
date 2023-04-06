
class Strange:
    def __hash__(self):
        return hash('hello')

    def __eq__(self, other):
        H.__bases__ = F,
        lst = []
        j = k = l = 42
        for i in range(100):
            lst.append((i, j, k, l))
        return False


class Y(object):
    pass

class X(Y, type):
    pass

class F:
    __metaclass__ = X

class G(F):
    pass

class H(G):
    pass

H.__dict__[Strange()] = 42

h = H()
h.hello

 	  	 
