import codecs
import csv

f = open('foo.csv', 'wb')
f.write(codecs.BOM_UTF8 + b'a,b,c')
f.close()

expected = ['a', 'b', 'c']
f = open('foo.csv')
r = csv.reader(f)
row = next(r)

print(row)
print(row == expected)