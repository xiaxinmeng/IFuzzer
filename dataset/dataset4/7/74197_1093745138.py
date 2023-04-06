# Initialize HTMLParser by loading htmlentitydefs
dummy = Dummy()
dummy.feed('<a href="&amp;">')
del dummy, Dummy