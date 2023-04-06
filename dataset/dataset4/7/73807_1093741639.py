import telnetlib

tn = telnetlib.Telnet('localhost')
tn.write('hello')