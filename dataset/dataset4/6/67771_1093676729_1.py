class U(unicode):
    def __unicode__(self):
        return u'U: ' + unicode.__unicode__(self)