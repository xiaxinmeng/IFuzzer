_setrecursionlimit = sys.setrecursionlimit
def setrecursionlimit(n):
    _setrecursionlimit(max(n, 50))
sys.setrecursionlimit = setrecursionlimit