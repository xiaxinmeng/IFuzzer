import locale
# LC_CTYPE: latin1 encoding
locale.setlocale(locale.LC_ALL, "en_GB")
# LC_MONETARY: utf8 encoding
locale.setlocale(locale.LC_MONETARY, "ar_SA.UTF-8")
lc = locale.localeconv()
for attr in (
    "mon_grouping",
    "int_curr_symbol",
    "currency_symbol",
    "mon_decimal_point",
    "mon_thousands_sep",
):
    print(f"{attr}: {lc[attr]!a}")