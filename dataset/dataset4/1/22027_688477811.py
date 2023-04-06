
a, i = 1, 0                     # line 1
while 1:                        # 2
    if i >= 3:                  # 3
        a = 4                   # 4
        break                   # 5
    i += 1                      # 6
assert a == 4 and i == 3        # 7
