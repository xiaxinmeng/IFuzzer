def printingdec(f):
    raise Exception()
    return f

def dummydec(f):
    return f

@printingdec
@dummydec
def foo():
    pass