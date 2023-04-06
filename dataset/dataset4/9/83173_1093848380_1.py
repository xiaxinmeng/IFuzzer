#######################
import math, dis

def test_fsum():
    x = [1.7**(i+1)-1.7**i for i in range(10)] + [-1.7**10]
    return x

y = test_fsum()
print(y)
print(math.fsum(y))
dis.dis(test_fsum)
#######################