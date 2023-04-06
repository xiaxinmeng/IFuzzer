r = dict(zip(s, range(len(s))), **d)
r = len(filter(attrgetter('t'), self.a))
r = min(map(methodcaller('f'), self.a))
max(map(node.id, self.nodes)) + 1 if self.nodes else 0
reduce(set.union, map(f, self.a))