F = ['2', '3', '1']
G = ['7', '9', '8']

def key(i):
    print(F)
    print(G)
    res = int(i) + len(F) + len(G)
    return res

G.sort(key=key)
F.sort(key=key)