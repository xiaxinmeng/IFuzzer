def foo():
    ldict = locals()
    exec("a=42",globals(),ldict)
    a = ldict['a']
    print(a)