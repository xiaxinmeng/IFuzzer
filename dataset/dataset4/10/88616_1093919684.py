def doit():
    o = ((1,2), (3,4))
    o = (a for
         a in
         o)
    for tup in o:
        x = tup[0]
        y = tup[1]