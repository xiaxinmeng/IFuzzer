class EuroHolder:
    def __init__(self, price):
        self._price = price
    def __str__(self):
        return "%.02f euro" % self._price
    def __unicode__(self):
        return u"%.02f\u20ac" % self._price