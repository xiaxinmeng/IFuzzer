import time
import locale
import pprint

time_tuple = time.struct_time((1999,3,17,1,44,55,2,76,0))

p1 = time.strftime("%p", time_tuple)
print("current LC_TIME", repr(p1))

locale.setlocale(locale.LC_TIME, ('de_DE', 'UTF8'))
p2 = time.strftime("%p", time_tuple)
print("de_DE (UTF8)", repr(p2))