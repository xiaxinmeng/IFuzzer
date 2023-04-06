class Metaklasse (type) :
    def __str__ (cls) :
        return 'string'
    def __unicode__ (cls) :
        return u'unicode'
    def __int__ (cls) :
        return 7

class Klasse :
    __metaclass__ = Metaklasse
    def __str__ (cls) :
        return 'text'
    def __unicode__ (cls) :
        return u'unicodetext'
    def __int__ (cls) :
        return 9