
# Replace LC_ALL with another category if you prefer
old_loc = locale.setlocale(locale.LC_ALL, None)
# ... code changing the locale ...
locale.setlocale(locale.LC_ALL, old_loc)
