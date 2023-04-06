import sys
print(sys.version_info)
import time 
print (time.strftime('%Y-%m-%d %H:%M:%S'))
fichin=open(r'D:\pythons\16s\total_gb_161_16S.gb')
start = time.time()
for i,li in enumerate(fichin):
    if i%1000000==0 and i>0: 
        print (i,time.time()-start)
fichin.close()
print(i)
print(time.time()-start)