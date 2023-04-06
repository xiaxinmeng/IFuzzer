sub(...)

# '"foo"' --> 'foo'
def remove_quotation_mark(s):
   return re.sub('^"(.*)"$', "\\1", s)