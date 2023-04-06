import numpy as np
import json

a = np.array([1,2,3,4])
json.dumps(a) #crash
json.dumps(a[0]) #this works!