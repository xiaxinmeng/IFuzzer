trans = []
for i in range(4):
    transrow = []
    for row in mat:
        transrow.append(row[i])
    trans.append(transrow)
print(trans)