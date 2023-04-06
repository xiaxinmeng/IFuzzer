bad = False
try:
    eval(default)
except NameError:
    pass # probably a named constant
except Exception as e:
    fail("Malformed expression given as default value\n"
         "{!r} raised {!r}".format(default, e))