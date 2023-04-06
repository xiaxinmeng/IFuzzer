from zipfile import ZipFile

zt=ZipFile("ziptest.zip","w")
zt.write("ziptest.py")
zt.write("ziptest.py")
zt.close()