#!python3
import time
import sys
with open('tzname_bug.txt', 'w', encoding='utf-8') as f:
    f.write(sys.version + '\n')
    f.write('Should be: Střední Evropa (běžný čas) | Střední Evropa (letní čas)\n')        
    f.write('but it is: ' + time.tzname[0] + ' | ' + time.tzname[1] + '\n')        
    f.write('    types: ' + repr(type(time.tzname[0])) + ' | ' + repr(type(time.tzname[1])) + '\n')
    f.write('Should be as ascii: ' + ascii('Střední Evropa (běžný čas) | Střední Evropa (letní čas)') + '\n')        
    f.write('but it is as ascii: ' + ascii(time.tzname[0]) + ' | ' + ascii(time.tzname[1]) + '\n')        