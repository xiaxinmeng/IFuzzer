for constructor in list, tuple, dict.fromkeys, set, collections.deque:
    container = constructor([float('nan'), 1, None, 'abc'])
    for elem in container :
         self.assert_(elem in container)