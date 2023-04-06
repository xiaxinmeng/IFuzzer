pycon
"""
>>> d = dict()
>>> id(d.fromkeys) == id(d.fromkeys)
True
>>> d.fromkeys is d.fromkeys
False
>>>
>>> id(dict.fromkeys) == id(dict.fromkeys)
True
>>> dict.fromkeys is dict.fromkeys
False
"""
