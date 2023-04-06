def icopysign(j,k):
    if (j > 0) and (k < 0) or (j < 0) and (k > 0):
        return -j
    return j
for j,k,i in ((1,1,1), (1,-1,-1), (-1,-1,-1), (-1, 1, 1),
              (1,0,1), (-1,0,-1)):
    assert icopysign(j,k) == i, (j,k,i)