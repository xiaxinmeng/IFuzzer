def func1():
    a=0 
    b=10
    for i in range(4):
        result = yield a+100 if b>100 else (yield a)
        print(result)

f1 = func1()
print("value:%s" % next(f1))
print("--------------")
print("value:%s" % next(f1))
print("--------------")