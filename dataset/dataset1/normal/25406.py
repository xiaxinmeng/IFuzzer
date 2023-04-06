import collections
x = collections.OrderedDict([ ('a', 1), ('b', 2), ('c', 3) ])
x.move_to_end('c', last = False)
x.move_to_end('a', last = False)
x
