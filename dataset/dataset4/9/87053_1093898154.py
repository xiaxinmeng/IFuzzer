mystr  = "hello123"
for x in range(1000000):
    mystr = mystr.__sizeof__()
    print(mystr)