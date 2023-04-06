myClib.getNumber.restype = c_long
myClib.doSomething.args = [c_long]
l = myClib.getnumber()
myClib.doSomething(l)