import re

a = unichr(0x2039)
b = u"["+re.escape(a)+u"]"
re.compile(b)