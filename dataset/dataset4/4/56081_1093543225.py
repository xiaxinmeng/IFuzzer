from numpy import *
import cPickle

a = zeros((300000, 1000)) 
f = open("test.pkl", "w") 
cPickle.dump(a, f)