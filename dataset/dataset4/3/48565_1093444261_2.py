def f(x):
    d ={"setting1":setting1,"setting2":setting2}
    exec(x) in d
    return d['setting1'], d['setting2']