b = B()
try:
    if b: pass
except:
    print("This won't happen, but it used to")