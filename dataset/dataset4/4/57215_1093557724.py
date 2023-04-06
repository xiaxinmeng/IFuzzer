import pickle
h = open('combined_oplists_pickle','r')
combined_oplists = pickle.Unpickler(h).load()
import pybugreport
funclist,funcdist = pybugreport.buildfunclist(combined_oplists)