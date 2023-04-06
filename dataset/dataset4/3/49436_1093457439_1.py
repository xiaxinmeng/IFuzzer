def a(size, shift):
    return len(set((id(o) >> shift) % (size * 2) for o in [object() for
i in range(size)]))

def b(size):
    return [a(size, shift) for shift in range(11)]

def c():
    for i in range(1, 9):
        size = 2**i
        x = ', '.join('% 3s' % count for count in b(size))
        print('% 3s: %s' % (size, x))