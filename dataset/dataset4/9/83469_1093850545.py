def nextAwayFromZero(x):
    if x < 0:
        return math.nextafter(x, -float("inf"))
    else:
        return math.nextafter(x, +float("inf"))