class X:
    def __init__(self,x):
        self.val = x
    def __add__(x,y):
        return X(x.val + y.val)
    def __radd__(x,y): return y + x

if __name__ == '__main__':
    x = X(4)
    y = 3 + x