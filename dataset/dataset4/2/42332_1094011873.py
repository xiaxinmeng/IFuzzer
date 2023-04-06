import locale, time
locale.setlocale(locale.LC_TIME, 'de_DE')
date = u'September'; format = '%B'
time.strptime(date, format)