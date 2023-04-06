import re

class MyUnicode(unicode):
   pass

val = MyUnicode("foobar")

r = re.compile(val)
#