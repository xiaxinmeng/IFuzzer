import json

class pseudo_list(object):
    __class__ = list # fake isinstance

    def __init__(self, iterator):
        self._saved_iterator = iterator

    def __iter__(self):
        return self._saved_iterator

class myenc(json.JSONEncoder):
    def default(self, o):
        try:
            return pseudo_list(iter(o))
        except TypeError:
            return super(myenc, self).default(o)