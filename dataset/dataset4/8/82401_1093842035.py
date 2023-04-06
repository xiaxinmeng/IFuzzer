import locale
from datetime import datetime
locale.setlocale(locale.LC_ALL, 'ca_AD.utf8')
locale.setlocale(locale.LC_ALL, 'ca_ES.utf8')
#locale.setlocale(locale.LC_ALL, 'es_ES.utf8')
now = datetime.now() # current date and time
date_time = now.strftime("|%b|%B|")
print("date and time:",date_time)