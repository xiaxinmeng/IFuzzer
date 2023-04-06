import locale, time
locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
t = time.localtime()
s = time.strftime('%c', t)
time.strptime('%c', s)