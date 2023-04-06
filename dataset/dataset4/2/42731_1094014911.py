import sys, unicodedata
spaces = u"".join(unichr(c) for c in xrange(0,
sys.maxunicode) if unicodedata.category(unichr(c))=="Zs" and
c != 160)
foo.split(spaces)