o= [1,2,3,3]
print('o:',id(o))
d= o
print('d:',id(d))
d= [1,2,3,4]
dd= o
print('dd:',id(dd))
dd[3]= 5

print('o:',o)
print('d:',d)
print('dd:',dd)