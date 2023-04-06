def prec_log(x, y):
    a = math.log(x, y)
    return a + math.log(x / math.pow(y, a), y)