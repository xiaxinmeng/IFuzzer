import time
fmt = '%d-%b-%y %H:%M:%S'
print(time.mktime(time.strptime('09-Mar-14 02:00:00',fmt)))