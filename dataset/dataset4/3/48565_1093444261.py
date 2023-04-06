setting1 = "val1"
setting2 = "val2"

def dummy():
    global setting1

def f(x):
    exec(x)
    return setting1,setting2