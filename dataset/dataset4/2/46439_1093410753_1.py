conv = converters.get(c)
if conv is None:
   y = list(x)
else:
   y = map(conv, x)