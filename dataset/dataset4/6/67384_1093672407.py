import locale
locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
a = ["A", "E", "Z", "a", "e", "é", "z"]
sorted(a)
sorted(a, key=locale.strxfrm)