import string
template = u""
result = string.Formatter().format(template)
assert isinstance(result, unicode)
# AssertionError