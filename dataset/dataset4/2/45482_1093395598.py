#######################
import time 
print (time.localtime())
fichin=open(r'D:\pythons\16s\total_gb_161_16S.gb')
t0= time.localtime()
print (t0)
i=0

for li in fichin:
	i+=1
	if i%1000000==0: 
		print (i,time.localtime())
	
fichin.close()
print ()
print (i)
print (time.localtime())
#########################