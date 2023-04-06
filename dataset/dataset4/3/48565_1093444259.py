setting1 = "val1"
setting2 = "val2"

def dummy():
    global setting1

def f(x):
    d ={"setting1":setting1,"setting2":setting2}
    exec(x) in d
    return d['setting1'], d['setting2']