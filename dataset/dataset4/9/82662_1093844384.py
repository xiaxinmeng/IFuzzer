class D:
    num = 0
    def __init__(self):
        D.num += 1
        print('D num', self.num)

for i in range(5):
    D()