class X:
    def __bool__(self):
        return True

x = [1, 2, 3]
x.sort(reverse=X())
print(x)
print(sorted([1, 2, 3], reverse=X()))