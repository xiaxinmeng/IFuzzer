class UnicodeAwareException(Exception):

    def __unicode__(self):
        return u" ".join(map(unicode, self.args))