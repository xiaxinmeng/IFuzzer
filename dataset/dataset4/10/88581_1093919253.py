for x in range(500):
  print(x)
  print ("something")
  sys.stdout.flush()
self.logger.info("A")
sys.stdout.flush()     #1 
self.logger.info("B")
print ("Hello")        #2
self.logger.info("C")
print ("Bye")          #3
self.logger.info("D")