def foo():
    try:
        yield
    except:
        print("!!! WE SHOULDN'T BE HERE!!!")

x = foo()
try:
    for _ in x:
       print(i)
except NameError:
    pass 

print("LOOP DONE")
del x   # <--- We shouldn't be here printed on this line.
print("FINAL")