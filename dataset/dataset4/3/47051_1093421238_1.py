import locale
locale.setlocale(locale.LC_ALL, "")
separator = locale.localeconv()["thousands_sep"]

def n_format(integer, separator):
    chars = []
    for i, char in enumerate(reversed("{0:d}".format(integer))):
        if i and not i % 3:
            chars.insert(0, separator)
        chars.insert(0, char)
    return "".join(chars)