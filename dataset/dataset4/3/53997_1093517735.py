import atexit

@atexit.register
def goodbye1():
    print(1)
    
@atexit.register
def goodbye2():
    print(2)