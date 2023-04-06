
a = 4

class A:
    a = a

print(A.a)

def createB(b):
    class B:
        z = b
    print(B.z)
    
createB(5)

def createD(D):
    class D:
        d = d
    print(D.d)
    
createD(6)
