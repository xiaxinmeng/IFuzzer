c = [(1, 10), (2, 20)]

# get a tuple with the first entries of every tuple in c,
# i.e. (1, 2)
x = zip(*c)[0]