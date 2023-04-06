import urllib2
f = urllib2.urlopen('http://www.google.com')
text=f.read()
f.fp._sock.recv=None # hacky avoidance
f.close()