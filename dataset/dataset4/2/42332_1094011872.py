import locale, time
locale.setlocale(locale.LC_TIME, 'de_DE')
date = u'10. September 2005 um 17:26'
format = '%d. %B %Y um %H:%M'
time.strptime(date, format)