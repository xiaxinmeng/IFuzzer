import locale, os
for l in open("/usr/share/i18n/SUPPORTED"):
    alias, encoding = l.strip().split()
    locale.setlocale(locale.LC_ALL, alias)
    try:
        enc = locale.getlocale()[1]
    except ValueError:
        continue # not in table
    normalized = enc.replace("ISO", "ISO-"). \
                     replace("_", "-"). \
                     replace("euc", "EUC-"). \
                     replace("big5", "big5-").upper()
    assert normalized == locale.nl_langinfo(locale.CODESET)