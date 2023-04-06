def g():
    x = yield + 1  # Yield the value +1
    y = (yield) + 1  # Add 1 after yielding
    return (yield)  # Mandatory brackets