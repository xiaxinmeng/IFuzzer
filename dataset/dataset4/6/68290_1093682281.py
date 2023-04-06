import codecs

class X(str):
    __class__ = UnicodeEncodeError

codecs.ignore_errors(X())