from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
     if 'EST' in line or 'EDT' in line:
         print(line)