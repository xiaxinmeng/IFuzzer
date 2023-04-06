# -*- coding: utf-8 -*-
# pickle_dump.py 
import datetime, pickle, uuid
dti = datetime.datetime(2015, 10, 12, 13, 17, 42, 123456)
data = { "ascii" : "abc", "text" : u"äbc", "int" :  42, "date-time" : dti }
with open("/tmp/pickle.test", "wb") as file :
    pickle.dump(data, file, protocol=2)

# pickle_load.py
# -*- coding: utf-8 -*-
import pickle
with open("/tmp/pickle.test", "rb") as file :
    data = pickle.load(file)
print(data)