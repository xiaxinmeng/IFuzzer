regex = None
def _has_surrogates(s):
    global regex
    if regex is None:
        regex = re.compile(short_regex)
    return regex.search(s)