# t is a tuple
h = INITIAL_VALUE
for x in t:
    z = hash(x)
    h = (h * MULTIPLIER) + z
return h