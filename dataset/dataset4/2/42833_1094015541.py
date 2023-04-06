import zipfile
z = zipfile.ZipFile("c:\\foo.zip","w")
z.write("c:\\autoexec.bat", "\\autoexec.bat")
z.close()