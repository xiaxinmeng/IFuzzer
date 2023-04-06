Point = colletions.namedtuple('Point', ['x', 'y', 'z'])
for proto in range(3):
    pickletools.dis(dumps(Point(10, 20, 30), proto))