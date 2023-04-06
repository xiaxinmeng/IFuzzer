pycon
"""
>>> d = {"{0}": "spam"}
>>> # a matched pair of braces. What's inside is considered markup.
... 
>>> "{0}".format(d)
"{'{0}': 'spam'}"
>>> # a matched pair of braces. Inside is a matched pair of braces, and what's inside of that is not considered markup.
"""
