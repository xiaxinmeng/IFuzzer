def _quote_periods(bindata):
    return re.sub(br'(?m)^\.', b'..', bindata)