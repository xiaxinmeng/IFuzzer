def a(**kwargs):
    pass

# this works
a(**{'b':'c'})

# this throws a format error
a(**{u'b':'c'})