x=1000
e="["*x+"]"*x
while 1:
    try:
        eval(e)
    except MemoryError:
        pass