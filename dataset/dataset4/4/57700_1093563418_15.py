def adapt_point(point):
   return ("%f;%f" % (point.x, point.y)).encode('ascii')

def convert_point(s):
   x, y = list(map(float, s.split(b";")))
   return Point(x, y)