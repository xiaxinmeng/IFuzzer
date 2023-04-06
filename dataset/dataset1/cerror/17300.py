from itertools import islice, count
it = count()
for i in range(1000000):
    it = islice(it, 0)
 
del it
