a = ['1','2','3']
b = [1,2,3]
c = zip(a,b)
print(dict(list(c))) #gives empty dict
print(dict(list(zip(a,b)))) #gives {'1':1,'2':2,'3':3}
d = zip(b,a)
print(dict(list(d))) #gives {1:'1',':'2',3:'3'}