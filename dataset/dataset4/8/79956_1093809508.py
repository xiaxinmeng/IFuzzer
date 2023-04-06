def _select(data, i, key=None):
    if not len(data):
        raise StatisticsError("select requires at least one data point")
    if not (1 <= i <= len(data)):
        raise StatisticsError(f"The index looked for must be between 1 and {len(data)}")
    data = sorted(data, key=key)
    return islice(data, i-1, None)

def select(data, i, key=None):
    return next(_select(data, y, key=key))