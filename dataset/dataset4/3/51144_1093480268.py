f = open("/var/lib/locales/supported.d/local")
locale_list = [loc.split()[0] for loc in f.readlines() \
               if not loc.startswith('#')]

for loc in locale_list:
    x = locale.setlocale(locale.LC_ALL, loc)
    try:
        y = locale.getlocale()
    except ValueError:
        print(loc)