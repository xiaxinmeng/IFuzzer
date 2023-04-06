pycon
"""
>>> d = dict()
>>> id(d.update) == id(d.update)
True
>>> d.update is d.update
False
>>>
>>> id(dict.update) == id(dict.update)
True
>>> dict.update is dict.update
True
"""
