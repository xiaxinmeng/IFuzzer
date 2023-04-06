class c_longdouble(_SimpleCData):
    _type_ = "g"
if sizeof(c_longdouble) == sizeof(c_double):
    c_longdouble = c_double