x = "xtop"
y = "ytop"
def func():
    x = "xlocal"
    y = "ylocal"
    class C:
        print(x)
        print(y)
        y = 1
func()