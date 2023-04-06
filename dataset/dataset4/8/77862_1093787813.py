import itertools

mylist = [(1,2), (1,3), (2,5)]

for key, igroup in itertools.groupby(mylist, lambda x: x[0]):
    print(list(igroup)) # prints the expected igroup
    print(list(igroup)) # prints an empty list
    print(list(igroup)) # prints an empty list