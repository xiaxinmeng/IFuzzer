pycon
#also: shouldn't ascii strings still work in Python 2.6.1 for
#StringIO and TextIO? As shown below, writes only work with unicode strings.
#Python 3 changes default encoding to utf-8 but 2.6.1 is still ascii:
#>>> import sys
#>>> sys.getdefaultencoding()
#'ascii'
