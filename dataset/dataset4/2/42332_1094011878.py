import locale, time
locale.setlocale(locale.LC_TIME, 'de_DE')
date = u'September'.encode()
format = '%B'
time.strptime(date, format)