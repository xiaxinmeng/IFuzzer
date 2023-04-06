import cgitb

class WeirdObject(object):
    def __getattr__(self, attr):
        if attr == 'a':
            return 'the letter a'
        elif attr == 'b':
            return str(slf) # Intentional NameError
        raise AttributeError(attr)