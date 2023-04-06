import sys
from Numeric import *
import cPickle

list = [{'name':'A', 'x':1}, {'name':'B', 'x':2}]

mask = [1,1]

rlist = compress( mask, list )
## rlist = rlist.tolist()    ## work-around

f = open( 'r.dat', 'w' )
r = cPickle.dump( rlist, f, 0) ## same with bin=1 or
pickle.dump
f.close()

sys.exit(0)

## RESTART PYTHON INTERPRETER HERE 
## (otherwise no segFault)
import cPickle

f = open( 'r.dat')
r = cPickle.load(f)  ## same with pickle.load
f.close()