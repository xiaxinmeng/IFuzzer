import telnetlib
tn = telnetlib.Telnet ("surfers.org", 4242)
tn.read_until ("Please enter your name:")
tn.write ("Mongo\n")
tn.read_until ("just connect to Surfers:")