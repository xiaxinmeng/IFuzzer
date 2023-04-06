import os, pwd
nobody = pwd.getpwnam('nobody')[2]
os.setuid(nobody)
open("dummy.txt", "w").write("foo") # permission denied