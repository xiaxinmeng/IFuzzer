def to_decimal(sec, nsec):
    return decimal.Decimal(sec) + decimal.Decimal(nsec).scaleb(-9)

def to_datetime(sec, nsec):
    # naive, we can do better
    t = sec + nsec*1e-9
    return datetime.datetime.fromtimestamp(t)

def to_float128(sec, nsec):
    return float128(sec) + float128(nsec)*float128(1e-9)