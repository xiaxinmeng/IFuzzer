def _get_empty(path):
    if isinstance(path, bytes):
        return b'' 
    else:
        return ''

def _get_sep(path):
    if isinstance(path, bytes):
        return b'\\'
    else:
        return '\\'

def _get_altsep(path):
    if isinstance(path, bytes):
        return b'/'
    else:
        return '/'

def _get_bothseps(path):
    if isinstance(path, bytes):
        return b'\\/'
    else:
        return '\\/'

def _get_dot(path):
    if isinstance(path, bytes):
        return b'.'
    else:
        return '.'