def f():
    try: return 0
    except: return 1,2

x = f() # x is 0
x,y = f() # proposal: x,y should be 1,2 instead of uncaught TypeError