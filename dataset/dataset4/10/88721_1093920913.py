
d = large_dict()
# remove all but one element of d, runs in quadratic time as explained above
while len(d) > 1:
    del d[next(iter(d))]

# now iterating over d takes O(d), even when d has only one item:

# the following prints one key, but takes O(N)
for key in d:
    print(key)
