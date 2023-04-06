def isfloat(s:str) -> bool:
    try:
        float(s)
        return True
    except:
        return False