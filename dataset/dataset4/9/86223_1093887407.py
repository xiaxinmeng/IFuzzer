
def callee():
    raise Exception

def caller():
    try:
        callee()
    except Exception or Exception:
        pass

caller()
