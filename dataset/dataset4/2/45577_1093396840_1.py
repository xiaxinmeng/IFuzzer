def doit():
   for i in xrange(0, 1000):
      p = subprocess.Popen( "true" )
      p.wait()

t = threading.Thread( target=doit )
t.start()
doit()