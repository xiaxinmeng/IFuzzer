def convert_to_unicode(mystr):
    if isinstance(mystr, unicode):
        return mystr
    if isinstance(mystr, str):
        return mystr.decode('utf8')