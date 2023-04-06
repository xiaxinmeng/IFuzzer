l_1 = [x] # one-element list
l_2 = l_1 * y # list with `y` times `x` in it (references to `x`, not copies)
l_3 = [l_2] # a new list with one element, `l_2`
l_4 = l_3 * n # list with `n` times `l_3` in it (references to `l_3`, not copies)