import sys
print(sys.version_info)
import time 
print (time.localtime())
fichin=open(r'D:\pythons\16s\total_gb_161_16S.gb')
start = time.time()
for i,li in enumerate(fichin):
    if i%1000000==0 and i>0: 
        print (i,start-time.time())
fichin.close()
print(i)
print(start-time.time())