#!/usr/bin/python
import pprint
pp = pprint.PrettyPrinter(indent=4)

myset = set(range(3))
myset.add(frozenset(range(10)))
pp.pprint(myset)
