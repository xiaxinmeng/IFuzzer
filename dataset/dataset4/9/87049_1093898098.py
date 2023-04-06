class A:
    def __init__(self, b=[]):
        print('b = ', b)
        self.a = b 

for i in range(3):
    a = A()
    a.a.append(1)

    print(a.a)