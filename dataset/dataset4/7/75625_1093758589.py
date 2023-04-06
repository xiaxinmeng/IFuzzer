import io
def _bad_TextIOWrapper(*args):
    return None
io.TextIOWrapper = _bad_TextIOWrapper
1/0