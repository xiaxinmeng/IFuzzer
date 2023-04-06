class MyClass:
     myattr = 0
inst = MyClass()
inst.myattr = 1
print(inst.__dict__["myattr"])