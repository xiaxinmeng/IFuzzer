from __future__ import print_function
import multiprocessing, logging
# # Activate multiprocessing logging
mplog = multiprocessing.get_logger()
mplog.setLevel(multiprocessing.util.DEBUG)
mplog.addHandler(logging.StreamHandler())
objs=[]
def newman(n=50):
    global objs
    m=multiprocessing.Manager()
    print('created')
    for i in range(n):
        objs.append(m.Value('i',i)) 
    return m    

print('#### first man')
m1=newman()