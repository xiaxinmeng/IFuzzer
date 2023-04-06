###Begin Script
import os

strPath = "c:/test.xxx"

#Create the file
f = open(strPath, 'w')
f.close()

#Set the file mod time
t1 = 1159195039.2
os.utime(strPath, (t1, t1))

#Get the file mod time
t2 = os.stat(strPath).st_mtime