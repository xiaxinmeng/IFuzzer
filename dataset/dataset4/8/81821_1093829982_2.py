
import telnetlib

tn = telnetlib.Telnet('127.0.0.1', 8888)
tn.interact()
