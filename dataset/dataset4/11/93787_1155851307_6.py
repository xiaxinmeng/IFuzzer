
# It's ill-advised to use variable names like this,
# but even if you do, that is still *some* way to get at them
__myglobal = 17
class A:
    print(globals()["__myglobal"])
# prints: 17
