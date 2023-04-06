class A(object):
    def __str__(self):
        return "str"
    def __unicode__(self):
        return "unicode"
    def __repr__(self):
        return "repr"

expression1 = False
expression2 = (A(),)