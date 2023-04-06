a = []
while True:
    x = u"x"*1000000
    x = x[30:60].simplify()  # Short slice of long string
    a.append(x)