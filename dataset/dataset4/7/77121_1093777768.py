from idlelib.pyparse import Parser
import timeit

class ParseGet(dict):
    def __getitem__(self, key): return self.get(key, ord('x'))
class ParseMis(dict):
    def __missing__(self, key): return ord('x')

for P in (ParseGet, ParseMis):
    print(P.__name__, 'hit', 'miss')
    p = p=P({i:i for i in (10, 34, 35, 39, 40, 41, 91, 92, 93, 123, 125)})
    print(timeit.timeit(
        "p[10],p[34],p[35],p[39],p[40],p[41],p[91],p[92],p[93],p[125]",
        number=100000, globals = globals()))
    print(timeit.timeit(
        "p[11],p[33],p[36],p[45],p[50],p[61],p[71],p[82],p[99],p[125]",
        number=100000, globals = globals()))