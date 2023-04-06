import csv

f = open('foo.csv', 'w')
w = csv.writer(f)
g = (i for i in ['a', 'b', 'c'])
w.writerow(list(g))
g = (i for i in ['a', 'b', 'c'])
w.writerow(g)