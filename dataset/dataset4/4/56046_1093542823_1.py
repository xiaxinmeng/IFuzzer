def _quote_periods(bindata):
    return re.sub(br'(?m)^\.', '..', bindata)