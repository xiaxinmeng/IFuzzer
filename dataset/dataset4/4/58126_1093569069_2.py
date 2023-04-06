def _anormalize(string):
    "remove thousands separators, make decimal dot"
    ts = localeconv()['thousands_sep']
    if ts:
        string = string.replace(ts, '')
    #next, replace the decimal point with a dot
    dd = localeconv()['decimal_point']
    if dd:
        string = string.replace(dd, '.')
    return string

def atof(string):
    "Parses a string as a float according to the locale settings."
    return float(_anormalize(string))

def atoi(string):  # changed from str
    "Converts a string to an integer according to the locale settings."
    return int(_anormalize(string))