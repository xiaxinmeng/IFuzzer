def f1():
    file1 = open("/dev/null")

def f2():
    file2 = open("/dev/null")
    del file2  # ResourceWarning

f1()  # ResourceWarning at function exit
f2()