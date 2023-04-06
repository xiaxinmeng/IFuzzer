     
f=file("/etc/passwd","r")
f.read(10)
f.flush()
f.close()