##########################
import threading
import os

class TestPopen( threading.Thread ):

   def run( self ):
      while 1:
         f = os.popen( "ls -l /" )
         lines = f.read()
         f.close()

if __name__ == "__main__":
   for i in range(50):
      t = TestPopen()
      t.start()
###########################