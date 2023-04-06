
a = b = c = 1
while not (a < b < c):
    if c == 1:
        c = 3
    else:
        b = 2
    print(a, b, c)
