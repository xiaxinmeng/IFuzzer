l=[1,3,2]
l.sort(cmp=lambda x,y:y-x, key=lambda x: x)
print(l)