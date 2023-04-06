# An undocumented, backwards compatible, API for all the places in the standard
# library that expect to be able to use tokenize with strings
def generate_tokens(readline):
    return _tokenize(readline, None)