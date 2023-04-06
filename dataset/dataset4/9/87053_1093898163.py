mystr  = "hello123"
print(dir(mystr))
for x in range(1000000):
    mystr = mystr.__class__
    print(mystr)