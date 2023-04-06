def convert_point(s):
    x, y = map(float, s.split(";"))
    return Point(x, y)