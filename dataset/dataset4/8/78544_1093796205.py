@dataclass
class C:
    f: 'Any'

T = namedtuple('T', 'a')

c = C({T('an a'): 0})
print('c:', c)
print(asdict(c))   # <- error here