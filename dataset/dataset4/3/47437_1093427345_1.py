import os

for Dir, SubDirs, Files in os.walk('/home/jarausch') :
  print("processing {0:d} files in {1}".format(len(Files),Dir))